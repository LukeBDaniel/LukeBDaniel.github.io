#!/usr/bin/env python3
"""
Automatically inject plt.savefig() and Image() calls after plot commands in Jupyter notebooks.
This script processes notebooks before nbconvert to automatically save and display plots.
"""

import json
import sys
import re
import os
from pathlib import Path

def extract_notebook_base_name(notebook_path):
    """Extract the base name from notebook path (e.g., '2025-7-25-Jets' from 'notebooks/2025-07-25 Jets/2025-7-25-Jets.ipynb')"""
    notebook_path = Path(notebook_path)
    base_name = notebook_path.stem  # Gets filename without extension
    return base_name

def detect_plot_commands(source_lines):
    """Detect if a cell contains plot commands that should have savefig/Image calls."""
    source_text = '\n'.join(source_lines)
    
    # Patterns that indicate plot creation (excluding savefig/show to avoid false positives)
    plot_patterns = [
        r'\.plot\s*\(',
        r'plt\.(plot|bar|barh|scatter|hist|boxplot|violinplot|pie|imshow|contour|contourf|pcolor|pcolormesh|hexbin|quiver|streamplot|fill_between|fill_betweenx|stackplot|step|loglog|semilogx|semilogy|twinx|twiny|subplot|subplots|figure|gcf|gca|title|xlabel|ylabel|legend|grid|xlim|ylim|xticks|yticks|tick_params|tight_layout|subplots_adjust)',
        r'sns\.(lineplot|barplot|boxplot|violinplot|stripplot|swarmplot|catplot|pointplot|countplot|jointplot|pairplot|distplot|kdeplot|rugplot|lmplot|regplot|residplot|heatmap|clustermap|FacetGrid|PairGrid|JointGrid|set_style|set_context|set_palette|despine|color_palette|palplot|plotting_context|axes_style|set_theme|load_dataset)',
        r'fig\s*=\s*plt\.',
        r'ax\s*=\s*plt\.',
        r'fig\s*=\s*plt\.figure',
        r'ax\s*=\s*fig\.',
    ]
    
    # Check if any plot pattern exists
    has_plot = any(re.search(pattern, source_text, re.IGNORECASE) for pattern in plot_patterns)
    
    return has_plot

def remove_existing_savefig_image(source_lines):
    """Remove existing plt.savefig() and Image() calls to avoid duplicates."""
    new_lines = []
    i = 0
    while i < len(source_lines):
        line = source_lines[i]
        line_text = line.strip()
        
        # Skip plt.savefig lines
        if re.search(r'plt\.savefig\s*\(', line_text, re.IGNORECASE):
            i += 1
            continue
        
        # Skip Image(filename=...) lines
        if re.search(r'Image\s*\(filename\s*=', line_text, re.IGNORECASE):
            i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    return new_lines

def generate_image_filename(notebook_base, cell_index, existing_names):
    """Generate a unique image filename based on notebook name and cell index."""
    # Try to find a descriptive name from the cell content
    base_name = notebook_base
    
    # Generate filename: {notebook_base}_plot_{cell_index}.png
    filename = f"{base_name}_plot_{cell_index}.png"
    
    # Ensure uniqueness
    counter = 1
    while filename in existing_names:
        filename = f"{base_name}_plot_{cell_index}_{counter}.png"
        counter += 1
    
    return filename

def inject_savefig_and_image(source_lines, notebook_base, cell_index, existing_names):
    """Inject plt.savefig() and Image() calls at the end of a cell."""
    # First, remove any existing savefig/Image calls
    source_lines = remove_existing_savefig_image(source_lines)
    
    # Generate image filename
    image_filename = generate_image_filename(notebook_base, cell_index, existing_names)
    existing_names.add(image_filename)
    
    # Create the path relative to notebook location
    # Notebooks are in subdirectories like "notebooks/2025-07-25 Jets/"
    # Images should go to "../assets/images/{base}/"
    image_path = f"../assets/images/{notebook_base}/{image_filename}"
    
    # Create savefig and Image lines
    savefig_line = f"plt.savefig('{image_path}', bbox_inches='tight')\n"
    image_line = f"Image(filename='{image_path}')"
    
    # Find the last non-empty line
    last_non_empty = len(source_lines) - 1
    while last_non_empty >= 0 and not source_lines[last_non_empty].strip():
        last_non_empty -= 1
    
    # Insert after the last non-empty line
    if last_non_empty >= 0:
        # Check if last line ends with a newline
        if not source_lines[last_non_empty].endswith('\n'):
            source_lines[last_non_empty] += '\n'
        
        # Insert savefig and Image calls
        source_lines.insert(last_non_empty + 1, savefig_line)
        source_lines.insert(last_non_empty + 2, image_line)
    else:
        # Cell is empty, just append
        source_lines.append(savefig_line)
        source_lines.append(image_line)
    
    return source_lines, image_filename

def ensure_image_import(notebook):
    """Ensure Image is imported from IPython.display."""
    has_import = False
    
    # Check all cells for Image import
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') != 'code':
            continue
        source = cell.get('source', [])
        if isinstance(source, str):
            source_text = source
        else:
            source_text = '\n'.join(source)
        
        if re.search(r'from\s+IPython\.display\s+import\s+Image', source_text, re.IGNORECASE):
            has_import = True
            break
    
    # Add import to first code cell if missing
    if not has_import:
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, str):
                    source_lines = source.splitlines(keepends=True)
                else:
                    source_lines = source
                
                # Add import at the beginning
                import_line = "from IPython.display import Image\n"
                if source_lines and not source_lines[0].startswith('from IPython.display import Image'):
                    source_lines.insert(0, import_line)
                    cell['source'] = source_lines
                    return True
                break
    
    return False

def process_notebook(notebook_path):
    """Process a notebook to inject automatic savefig/Image calls."""
    notebook_path = Path(notebook_path)
    
    if not notebook_path.exists():
        print(f"Error: Notebook not found: {notebook_path}", file=sys.stderr)
        return False
    
    # Read notebook
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"Error reading notebook {notebook_path}: {e}", file=sys.stderr)
        return False
    
    # Extract base name for image paths
    notebook_base = extract_notebook_base_name(notebook_path)
    
    # Track existing image filenames to avoid duplicates
    existing_names = set()
    
    # Track if we made any changes
    modified = False
    
    # Ensure Image import exists
    if ensure_image_import(notebook):
        modified = True
        print(f"  Added Image import")
    
    # Process each cell
    for cell_index, cell in enumerate(notebook.get('cells', [])):
        if cell.get('cell_type') != 'code':
            continue
        
        source = cell.get('source', [])
        if isinstance(source, str):
            source_lines = source.splitlines(keepends=True)
        else:
            source_lines = source
        
        # Check if this cell needs savefig/Image injection
        if detect_plot_commands(source_lines):
            source_lines, image_filename = inject_savefig_and_image(source_lines, notebook_base, cell_index, existing_names)
            cell['source'] = source_lines
            modified = True
            print(f"  Injected savefig/Image for plot in cell {cell_index}: {image_filename}")
    
    # Write back if modified
    if modified:
        try:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error writing notebook {notebook_path}: {e}", file=sys.stderr)
            return False
    
    return False

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 auto_save_plots.py <notebook1.ipynb> [notebook2.ipynb ...]", file=sys.stderr)
        sys.exit(1)
    
    success_count = 0
    for notebook_path in sys.argv[1:]:
        if process_notebook(notebook_path):
            success_count += 1
    
    if success_count > 0:
        print(f"Successfully processed {success_count} notebook(s)")
    else:
        print("No notebooks were modified")

if __name__ == '__main__':
    main()


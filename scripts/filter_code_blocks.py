import sys

md_path = sys.argv[1]

in_code = False
keep = False
output = []
block = []

with open(md_path) as f:
    for line in f:
        if line.startswith("```"):
            if in_code and keep:
                # Remove the tag line before writing
                cleaned_block = [l for l in block if "# INCLUDE" not in l]
                output.extend(cleaned_block)
                output.append(line)
            elif not in_code:
                block = [line]
            in_code = not in_code
            keep = False
            continue
        if in_code:
            block.append(line)
            if "# INCLUDE" in line:
                keep = True
        else:
            output.append(line)

with open(md_path, "w") as f:
    f.writelines(output)

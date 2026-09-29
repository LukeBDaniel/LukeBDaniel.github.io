# Blog research files

Each dated folder contains the source notebook and any inputs for one published
analysis. The corresponding reader-facing article is in `src/content/blog/`.
Editing a notebook or its export does not update the website article.

`exports/` in each folder holds the Markdown export and its matching `_files/`
image directory. Keep those two items together: the export uses relative links
to its images. If you regenerate an export, place both new outputs in that
folder and inspect the diff before replacing the archived version. Other images
in a research folder may be inputs or working files and should not be removed
just because a chart also appears in `public/assets/images/`.

Images used by the site live in `public/assets/images/`. Their URLs appear in
the published Markdown, so moving them requires updating those references and
considering existing links to the images.

`modern_overtime_charts.py` generates charts for the overtime article directly
in the site's public image directory. It is source code, not an export.
`scripts/auto_save_plots.py` also generates site image paths when it updates a
notebook; run the notebook from its dated folder so those relative paths resolve.

# Luke Daniel - Personal Portfolio

Welcome to the repository for my personal portfolio website!

**Live Site:** [https://LukeBDaniel.github.io](https://LukeBDaniel.github.io)

This website is built to serve as a central hub for my projects, resume, and short data analysis posts.

## Fourth Down Calculator

The project page at `/projects/fourth-down-calc/` embeds the static calculator
at `/fourth-down-calc/`. Its published bundle is checked into
`public/fourth-down-calc/`, so the existing GitHub Pages deployment is self-contained.
The bundle includes model attribution, game schedules, team/kicker ratings, and
the historical fourth-down archive. The game browser loads these as static JSON,
so no server API is needed. The calculator is still in development.

To refresh it from the sibling `fourth-down-calc` checkout (with its dependencies
installed and Node 22.13+):

```sh
node scripts/update-fourth-down.mjs
npm run build
```

An alternate source checkout can be passed as the script's first argument.
The calculator's `STATIC_ASSET_PREFIX` option sets asset and model URLs without
the upstream static export's `BASE_PATH` prerendering issue. Only public browser
assets are copied; server build files and local configuration stay out of the site.

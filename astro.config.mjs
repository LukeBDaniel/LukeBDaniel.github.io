import mdx from '@astrojs/mdx';

import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	site: 'https://lbdaniel.com',
	integrations: [mdx()],
	markdown: {
		syntaxHighlight: false,
	},
});

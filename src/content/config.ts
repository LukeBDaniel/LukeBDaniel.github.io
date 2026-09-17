import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
	type: 'content',
	// Type-check frontmatter using a schema
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			// Transform string to Date object
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: z.optional(image()),
			thumbnail: z.string().optional(),
			thumbnailAlt: z.string().optional(),
			thumbnailWidth: z.number().optional(),
			thumbnailHeight: z.number().optional(),
		}),
});

export const collections = { blog };

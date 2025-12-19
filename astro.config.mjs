import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap'; // Add this line

export default defineConfig({
  site: 'https://your-site-name.netlify.app',
  base: '/',
  output: 'static',
  integrations: [
    tailwind(), 
    sitemap() // Add this line
  ],
});
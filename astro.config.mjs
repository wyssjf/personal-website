import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  // Final Netlify URL
  site: 'https://jaywyss.netlify.app', 
  base: '/', 
  output: 'static', 
  integrations: [
    tailwind(),
    sitemap(),
  ],
});
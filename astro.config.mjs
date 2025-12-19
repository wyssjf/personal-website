import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap'; // Optional: if you want a sitemap

// https://astro.build/config
export default defineConfig({
  // SITE URL: Astro uses this for sitemaps and canonical URLs.
  // Netlify will automatically handle this if you leave the placeholder below.
  site: 'https://your-site-name.netlify.app', 

  // BASE PATH: Set to '/' for root-level deployment on Netlify subdomains.
  base: '/', 

  // OUTPUT MODE: 'static' is standard for Astro personal websites.
  output: 'static', 

  // INTEGRATIONS: Ensure tailwind() is listed here.
  integrations: [
    tailwind(),
    sitemap(), // Remove if not using @astrojs/sitemap
  ],
});
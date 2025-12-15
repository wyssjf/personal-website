// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind"; // KEEP YOUR INTEGRATIONS (if you use tailwind)

export default defineConfig({
    // VERCEL FIX: Provide a valid URL for your code to use for canonical links/sitemap
    site: 'https://personal-website-oaae8htiy-jay-wyss-projects.vercel.app', 
    
    // VERCEL FIX: Setting base to '/' tells Astro assets are at the root
    base: '/', 
    
    output: 'static', 

    integrations: [tailwind()] // KEEP YOUR INTEGRATIONS
});
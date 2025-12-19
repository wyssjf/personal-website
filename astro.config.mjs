// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

export default defineConfig({
    // Use a placeholder; Netlify will override this with your actual URL
    site: 'https://your-site-name.netlify.app', 
    base: '/', 
    output: 'static',
    integrations: [tailwind()],
});
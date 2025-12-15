// astro.config.mjs
import { defineConfig } from 'astro/config';

export default defineConfig({
    // VERCEL FIX: Setting base to '/' tells Astro assets are at the root
    base: '/', 
    
    // VERCEL FIX: Remove the GitHub Pages 'site' property entirely
    // site: 'https://wyssjf.github.io', // DELETE THIS LINE
    
    output: 'static', 

    // ... (keep any other integrations you have below)
});
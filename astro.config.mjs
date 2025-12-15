// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind"; // KEEP YOUR INTEGRATIONS

export default defineConfig({
    // 1. ADD THIS BACK, BUT POINT TO THE VERCEL ROOT DOMAIN
    site: 'https://personal-website-oaae8htiy-jay-wyss-projects.vercel.app', 
    
    // 2. KEEP THIS VERCEL FIX
    base: '/', 
    
    output: 'static', 

    integrations: [tailwind()] // KEEP YOUR INTEGRATIONS
});
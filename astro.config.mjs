// astro.config.mjs
import { defineConfig } from 'astro/config';

export default defineConfig({
    // MUST be the full domain root
    site: 'https://wyssjf.github.io', 
    
    // MUST be the repository name with slashes
    base: '/personal-website/', 
    
    output: 'static', 

    // ... (any other integrations you have)
});
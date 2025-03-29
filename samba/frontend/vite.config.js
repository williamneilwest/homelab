import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';
export default defineConfig({
  root: './src',  // Example: set your root directory
  build: {
    outDir: 'dist',
  },
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 3001,
  },
});

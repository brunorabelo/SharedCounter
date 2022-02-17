import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig(({command, mode})=> {
  var config = {
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
  }
  if (mode === 'development'){
    config.server = {
      proxy:{
      // with options
        '/api': {
          target: "http://localhost:8000",
          changeOrigin: true,
          secure: false
        },
        '/admin': {
          target: "http://localhost:8000",
          changeOrigin: true,
          secure: false
        },
      }
    }
  }
  return config
})

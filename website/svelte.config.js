import adapter from '@sveltejs/adapter-static';
import * as process from ".svelte-kit/ambient.js";
export default {
  kit: {
    adapter: adapter(),
    paths: {
      base: process.env.NODE_ENV === "production" ? "/Space_Dodge" : "",
    }
  }
}
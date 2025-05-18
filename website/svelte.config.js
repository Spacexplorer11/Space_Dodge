import adapter from '@sveltejs/adapter-static';
export default {
  kit: {
  adapter: adapter(),
  paths: {
    base: process.env.NODE_ENV === 'production' ? '/Space_Dodge' : '',
  }
}
}

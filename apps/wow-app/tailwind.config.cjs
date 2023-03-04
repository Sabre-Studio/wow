/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/app/**/*.{js,ts,jsx,tsx}',
    './src/components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('windy-radix-palette'),
    require('tailwindcss-radix')(),
    require('@tailwindcss/typography'),
    require('windy-radix-typography'),
    require('@tailwindcss/forms'),
  ],
}

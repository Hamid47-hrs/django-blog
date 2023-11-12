/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

// $ cd app
// $ npx tailwindcss -i assets/styles/input.css -o assets/styles/output.css --watch
const defaultTheme = require('tailwindcss/defaultTheme');
const formsPlugin = require('@tailwindcss/forms');

module.exports = {
  darkMode: 'class',
  content: ['./src/**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Albert Sans', ...defaultTheme.fontFamily.sans],
        serif: 'Palatino, "Palatino Linotype", "Book Antiqua", "Hoefler Text", Georgia, "Lucida Bright", Cambria, Times, "Times New Roman", serif',
      },
    },
  },
  plugins: [
    formsPlugin,
  ],
};

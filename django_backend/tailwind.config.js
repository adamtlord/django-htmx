const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  darkMode: 'class',
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Albert Sans', ...defaultTheme.fontFamily.sans],
      },
    }
  },
  plugins: [],
}

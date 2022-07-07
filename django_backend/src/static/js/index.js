/* global Alpine */

const App = () => ({
  darkMode: localStorage.getItem('dark') === 'true' || (!('dark' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches),
  toggleDarkMode() {
    const currentVal = this.darkMode;
    this.darkMode = !currentVal;
    localStorage.setItem('dark', !currentVal);
  },
});

document.addEventListener('alpine:init', () => {
  Alpine.data('App', App);
});

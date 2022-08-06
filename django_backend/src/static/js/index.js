/* global Alpine */

const App = () => ({
  darkMode: localStorage.getItem('dark') === 'true' || (!('dark' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches),
  sidebarOpen: false,
  profileDropdown: false,
  activeNav: '',
  toggleDarkMode() {
    const currentVal = this.darkMode;
    this.darkMode = !currentVal;
    localStorage.setItem('dark', !currentVal);
  },
  init() {
    this.activeNav = window.location.pathname.split('/')[window.location.pathname.split('/').length - 1];
  },
});

document.addEventListener('alpine:init', () => {
  Alpine.data('App', App);
});

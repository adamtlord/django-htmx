export default () => ({
  darkMode: localStorage.getItem('dark') === 'true',
  toggleDarkMode() {
    const currentVal = this.darkMode;
    this.darkMode = !currentVal;
    localStorage.setItem('dark', !currentVal);
  },
});

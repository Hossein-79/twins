// Dark mode
var darkMode = localStorage.getItem('darkMode');
var darkModeToggle = document.getElementById('dark-mode-checkbox');
if (darkMode === null) {
    setDarkMode(false);
} else {
    setDarkMode(darkMode === 'true');
}
function setDarkMode(isDark) {
    localStorage.setItem('darkMode', isDark);
    if (isDark) {
        document.querySelector('html').classList.add('dark');
        darkModeToggle.setAttribute('checked', true);
    } else {
        document.querySelector('html').classList.remove('dark');
        darkModeToggle.removeAttribute('checked');
    }
}
// Toggle dark mode
darkModeToggle.addEventListener('change', function () {
    setDarkMode(darkModeToggle.checked);
});
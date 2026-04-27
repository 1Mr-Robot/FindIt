document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn1 = document.getElementById('toggle-password-1');
    const toggleBtn2 = document.getElementById('toggle-password-2');
    const passwordInput1 = document.getElementById('login-pass-1');
    const passwordInput2 = document.getElementById('login-pass-2');

    if (toggleBtn1 && passwordInput1) {
        toggleBtn1.addEventListener('click', function() {
            const isPassword = passwordInput1.type === 'password';
            passwordInput1.type = isPassword ? 'text' : 'password';
            toggleBtn1.textContent = isPassword ? 'visibility_off' : 'visibility';
        });
    }

    if (toggleBtn2 && passwordInput2) {
        toggleBtn2.addEventListener('click', function() {
            const isPassword = passwordInput2.type === 'password';
            passwordInput2.type = isPassword ? 'text' : 'password';
            toggleBtn2.textContent = isPassword ? 'visibility_off' : 'visibility';
        });
    }
});
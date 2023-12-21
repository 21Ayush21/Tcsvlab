const forms = document.querySelectorAll(".form"),
eye = document.querySelectorAll(".eye-icon"),
links = document.querySelectorAll(".link");

eye.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let passField = eyeIcon.parentElement.parentElement.querySelectorAll(".password");

        passField.forEach(password => {
            if(password.type === 'password'){
                password.type = 'text';
                eyeIcon.classList.replace('bx-hide' , 'bx-show');
                return;
            }
            password.type = 'password';
            eyeIcon.classList.replace('bx-show' , 'bx-hide');
        })
    })
})
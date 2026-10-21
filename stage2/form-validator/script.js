const button = document.getElementById("button")

const fullname = document.getElementById("full-name")
const email = document.getElementById("email")
const password = document.getElementById("password")
const confirmpassword = document.getElementById("confirm-password")

const spans = document.querySelectorAll("span")

button.addEventListener("click" , function(){
    spans[0].textContent =""
    spans[1].textContent =""
    spans[2].textContent =""
    spans[3].textContent =""

    let valid = true

    if (fullname.value.trim().length < 3) {
        spans[0].textContent = "Name must be at least 3 characters"
        valid = false
    }
    if (!email.value.includes("@") || !email.value.includes(".")) {
        spans[1].textContent = "Enter a valid email address"
        valid = false 
    }
    if (password.value.length < 8){
        spans[2].textContent = "password must be at least 8 character"
        valid = false
    }
    if (confirmpassword.value === "" ||confirmpassword.value !== password.value) {
        spans[3].textContent = "passwords do not match "
        valid = false
    }
    if (valid) {
        spans[0].textContent = "Form summit sucessfully!"
        spans[0].style.color = "#00ff88"
    }
})

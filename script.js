// Practice query selector function
function changeColor(newColor) {
    const elem = document.getElementById("para");
    elem.style.color = newColor;
}

document.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", (event) => {
        changeColor(event.target.textContent.toLowerCase());
    });
});

// Show/hide authentication overlay
function authenticateUser(user) {
    const elem = document.getElementById("auth-overlay");
    elem.classList.toggle('hidden', !isLoggedIn);
}

document.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", (event) => {
        authenticateUser(event.target)
    })
})
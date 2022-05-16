var animalImg = document.querySelector("#fav-animal")
// console.log(animalImg)



function pickCat(element) {
    // console.log(element.style)
    element.style.backgroundColor = "goldenrod";
    animalImg.src = "Cat.png"
}

function pickDog(element) {
    element.classList.add("btn");
    animalImg.src = "Dog.png"
}

function setActive(element) {
    var background = document.querySelector("body")
    if(background.classList.contains("dark-mode")) {
        element.innerText = "Cambiar al modo oscuro";
        background.classList.remove("dark-mode");
    } else {
        element.innerText = "Cambiar al modo claro";        
        background.classList.add("dark-mode");
    }
    console.log(element.classList)
}
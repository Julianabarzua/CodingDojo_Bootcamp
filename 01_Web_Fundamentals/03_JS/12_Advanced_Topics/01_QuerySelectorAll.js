var colors = document.querySelectorAll(".color");
console.log(colors);


function applyColors(){
    
    for (var i=0; i < colors.length; i++) {
        console.log(i);
        colors[i].style.color = colors[i].innerText;
    }
}


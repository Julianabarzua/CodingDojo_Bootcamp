function loginlogout(element){
    if (element.innerText == "Login"){
        element.innerText = "Logout";
    }
    else {
        element.innerText = "Login";
    }
}

function remove(element){
    var el = element;
    el.remove();
}
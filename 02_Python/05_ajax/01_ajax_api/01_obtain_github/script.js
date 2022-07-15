var cardsDiv = document.querySelector("#cards");

function showinfo(data){
    var res =   `<h3>${data.name} has ${data.followers} followers </h3>
                <img src="${data.avatar_url}" alt="${data.login}">`
    return res;
}

async function search(){
    var response = await fetch("https://api.github.com/users/adion81");
    var coderData = await response.json();
    console.log(coderData);
    cardsDiv.innerHTML = showinfo(coderData);
}


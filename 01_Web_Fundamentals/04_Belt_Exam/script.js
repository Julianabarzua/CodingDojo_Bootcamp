let count = 0;
let version = "v4.3"

function changeVersion(element){

    temp = document.getElementById("version");
    temp.innerText = "DOWNLOAD VERSION "+element.value+" - TOTAL DOWNLOADS: "+count;

    temp2 = document.getElementById("btn2");
    temp2.innerText = "Download " + element.value;

    version = element.value;


}

function startingAlert(){

    alert("Loading Start Page")
}

function add1(){
    count +=1;
    temp = document.getElementById("version");
    temp.innerText = "DOWNLOAD VERSION "+version+" - TOTAL DOWNLOADS: "+count;
}
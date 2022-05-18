var req = 2;
var con = 480;

function remove(u){
    if(u == 1){
        var box = document.getElementById("todd");
    }
    
    else{
        var box = document.getElementById("phil");
    }
    
    req--;
    var ele = document.getElementById("reqnumber");
    ele.innerText = req;

    
    console.log(box);
    box.remove();

}

function removeANDadd(u){
    if(u == 1){
        var box = document.getElementById("todd");
    }
    
    else{
        var box = document.getElementById("phil");
    }
    
    req--;
    var ele = document.getElementById("reqnumber");
    ele.innerText = req;

    con++;
    var ele = document.getElementById("connumber");
    ele.innerText = con;
    
    console.log(box);
    box.remove();

}

var x = true;

function changeName(){
    var ele = document.getElementById("profile_name");

    if (x == true){
        ele.innerText = "Julián Abarzúa";
        x = false;
    }
    else {
        ele.innerText = "Jane Doe";
        x = true;
    }
}
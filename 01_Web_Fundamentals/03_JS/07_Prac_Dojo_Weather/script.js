function remove(){
    var ele = document.getElementById("cookies");    
    ele.remove();
}

var tempc=["24°","18°", "27°", "19°", "21°","16°", "26°", "11°"];
var tempf=["75°","65°", "80°", "66°", "69°","61°", "78°", "70°"];

function changeTemps(element){

    if(element.value == "C°"){
        console.log("C seleccionado");
        for(var y=0; y<tempc.length; y++){
            console.log(tempc[y])
            temp = document.getElementById("t"+y)
            temp.innerText = tempc[y]
        }
    }
    
    else{
        console.log("F seleccionado");
        for(var y=0; y<tempf.length; y++){
            console.log(tempf[y])
            temp = document.getElementById("t"+y)
            temp.innerText = tempf[y]
        }

        }
}
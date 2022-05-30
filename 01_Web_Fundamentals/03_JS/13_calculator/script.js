const displayDiv = document.querySelector("#display");

let num1 =""
let num2 =""
let op = ""

function press(n){
    num1 += n;
    displayDiv.innerHTML=num1;    
}

function clr(){
    num1 =""
    num2 =""
    op = ""
    displayDiv.innerText = 0;
}

function setOP(f){
    op = f;
    num2 = num1;
    num1 = "";
}

function calculate (){

    console.log (num1,num2,op)


    let x = parseFloat(num1);
    let y = parseFloat(num2);
    let r = 0;    
    if (op == "+"){
        r = x+y;
    }
    else if (op == "-"){
        r = y-x;
    }

    else if (op == "*"){
        r = y*x;
    }

    else if (op == "/"){
        r = y/x;
    }

    num1 = r;
    op="";
    displayDiv.innerText = r;
}
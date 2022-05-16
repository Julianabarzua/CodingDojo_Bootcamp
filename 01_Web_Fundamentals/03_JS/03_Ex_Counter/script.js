var count = 0;
var countElement = document.querySelector("#count");

console.log(countElement)

function add1() {
    count++;
    countElement.innerText = "The count is " + count;
    console.log(count);
}

function substract1() {
    count--;
    countElement.innerText = "The count is " + count;
    console.log(count);
}
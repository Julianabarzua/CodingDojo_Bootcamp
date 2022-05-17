var count=[9,12,9];

function addlike(x){
    count[x]++;

    for(var i=0; i<count.length; i++){
        var counter=document.querySelector("#like"+i);
        counter.innerText = count[i] + " like(s)";
    }
}
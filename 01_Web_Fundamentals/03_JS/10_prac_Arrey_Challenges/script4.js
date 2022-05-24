function reverse(arr) {
    let reverse=[];
    for(i=arr.length-1;i>=0;i--){
        
        reverse.push(arr[i]);
    }

    arr = reverse;
    return arr;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // esperamos de vuelta ["e", "d", "c", "b", "a"]

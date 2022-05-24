function betterThanAverage(arr) {
    
    var sum = 0;
    for(i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    let ave = sum/arr.length;
    console.log("ave="+ave)

    var count = 0
    for(i=0;i<arr.length;i++){
        if(arr[i] > ave ){
            count +=1
        }
    }    
    return count;
}



var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // esperamos 4 de vuelta

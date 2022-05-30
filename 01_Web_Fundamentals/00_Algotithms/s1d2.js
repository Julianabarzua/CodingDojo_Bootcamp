var a = 25;
a = a - 13;
console.log(a/2);
    
a = "hola";
console.log(a + " hola");




for(var i=0; i<10; i++) {
    console.log(i);
    i = i + 3; 
}
    
console.log("fuera del bucle " + i);





function getTotal(arrayOfNumbers) {
    
    var sum = arrayOfNumbers[0];
      
    for(var i=0; i<arrayOfNumbers.length; i++) {
      sum += arrayOfNumbers[i];
      console.log("la suma actual es: " + sum); 
    }
      
    console.log("el total es: " + sum);
      
  }
      
  getTotal([1, 3, 5]);
  


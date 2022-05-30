var contarPositivos = 0;
var numeros = [3, 4, -2, 7, 16, -8, 0];

for (let i=0; i<numeros.length; i++){
    if ( numeros[i]>0){
        contarPositivos++;
    }
}
    
console.log("hay " + contarPositivos + " valores positivos");

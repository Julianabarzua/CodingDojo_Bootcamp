function siempreHambriento(arr) {
    
    let haycomida = false;

    for (let i=0; i<arr.length; i++){
        if (arr[i] == "comida"){
            console.log("delicioso");
            haycomida = true;
        }
    }

    if (haycomida == false){
        console.log("tengo hambre");
    }

}



siempreHambriento([3.14, "comida", "pastel", true, "comida"]);
// esto debería mostrar "delicioso, "delicioso"
siempreHambriento([4, 1, 5, 7, 2]);
// esto debería mostrar "Tengo hambre"

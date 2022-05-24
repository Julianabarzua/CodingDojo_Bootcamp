function pizzaOven(tipoCorteza, tipoSalsa, quesos, salsas){
    var pizza = {};
    pizza.corteza = tipoCorteza;
    pizza.salsa = tipoSalsa;
    pizza.quesos = quesos;
    pizza.salsas = salsas;

    return pizza;
}

var p1=pizzaOven("estilo Chicago", "tradicional", ["mozzarella"] , ["pepperoni", "salchicha"]);
var p2=pizzaOven("lanzada a mano" , "marinara" , ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);
var p3=pizzaOven("delgada","crema con ajo", ["feta"], ["pollo","cebolla"]);
var p4=pizzaOven("bordequeso", "BBQ", ["Cheddar"], ["jamon", "pimenton", "champiñones"]);

console.log(p1)
console.log(p2)
console.log(p3)
console.log(p4)
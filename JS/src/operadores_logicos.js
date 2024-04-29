/*
&& AND (Conjunción lógica)
El resultado de hacer A && B será Verdadero únicamente cuando ambos operandos sean Verdaderos. 
Cualquier otro caso el resultado será falso.

A | B | A && B
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1

|| OR (Disyunción lógica)
El resultado de hacer A || B será Verdadero cuando al menos uno de los operandos sea verdadero.
El único caso donde es falso es cuando ambos operandos son falsos.

A | B | A || B
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 1

! NOT (Negación lógica)
invierte o niega el valor de un booleano.

A | !A
0 | 1
1 | 0

*/

/*
    Martin, un joven programador que se dirije a la cocina.
    Al pasar martin se pregunta dos cosas, si tiene hambre y si tene ganas de comer.

    Si tiene hambre y ganas de comer: se arma un sanguche.
    Si no tiene hambre y no tiene ganas de comer: se va dormir.
    Si tiene hambre y no tiene ganas de comer: se hace un té.
    Si no tiene hambre y si tiene ganas de comer: se come una mandarina.
*/

let hambre = true;
let comer = false;

// combinacion de ANDs y NOTs
if (hambre && comer) {
    console.log("Se arma un sanguche");
}

if(hambre && !comer) {
    console.log("Se hace un té");
}

if(!hambre && comer) {
    console.log("Se come una mandarina");
}

if (!hambre && !comer) {
    console.log("Se va a dormir");
}

// ifs anidados
if(hambre) {
    if(comer) {
        console.log("Se arma un sanguche");
    } else {
        console.log("Se hace un té");
    }
} else {
    if(comer) {
        console.log("Se come una mandarina");
    } else {
        console.log("Se va a dormir");
    }
}





/*
if (hambre) {
    console.log("Tiene hambre");

} else {
    console.log("No tiene hambre");
}

if(!hambre) {
    console.log("No tiene hambre");

} else {
    console.log("Tiene hambre");
}
*/
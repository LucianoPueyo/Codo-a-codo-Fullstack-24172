let contador = 0

let seguir = true;
let respuesta;

while(seguir) {
    respuesta = Number.parseInt(prompt("Ingrese un numero del 1 al 10"));

    if(respuesta >= 1 && respuesta <= 10) {
        seguir = false;
    }
}

console.log("la respuesta del usuario es: " + respuesta);

while(contador < 10){
    console.log(contador);
    contador++;
}

console.log("for -----------------------------");

// for (inicio; condicion; incremento)
for(i = 0; i < 10; i++){
    console.log(i);
}

console.log("ejemplo con listas -----------------------------");

let lista = ["Carlos", "Maria", "Jose", "Gaston", "Pedro", "Luisa"];

for(i = 0; i < lista.length; i++) {
    console.log(lista[i]);
}

console.log("while -----------------------------");

contador = 20;
while(contador < 10) {
    console.log(contador);
    contador++;
}
console.log("do while -----------------------------");

contador = 20;
do {
    console.log(contador);
    contador++;
}while(contador < 10);

console.log("Adios");
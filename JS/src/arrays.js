let nota = 7;

//         indice:  0  1  2   3
let nota_alumnos = [7, 8, 10, 9]; // Creando una nueva lista

// las listas son dinamicamente tipadas, por ende, pueden guardar valores de cualquier tipo
let lista2 = [15, "Hola", true, undefined, [1,2,3]];

console.log(nota_alumnos);    // consulto toda la lista
console.log(nota_alumnos[0]); // consultando el primer valor
console.log(nota_alumnos[nota_alumnos.length - 1]); // consultando el último valor

// ordenar un array

// funcion flecha
function metodo_ordenar(a, b){
    return a - b;
}

// estas dos formas hacen lo mismo, uno recibe una funcion clasica como criterio de ordenamiento y la segunda recibe una funcion flecha.
nota_alumnos.sort(metodo_ordenar);
nota_alumnos.sort((a,b) => a - b);

console.log(nota_alumnos);

// Modificando listas
nota_alumnos[0] = 8;
console.log(nota_alumnos);

// Agregando elementos
nota_alumnos[4] = 6.5;
console.log(nota_alumnos);

// Agregando valores fuera de rango
nota_alumnos[9] = 10;
console.log(nota_alumnos);

// Agregando al final de la lista
nota_alumnos.push(7);
nota_alumnos.push(8);
nota_alumnos.push(9);
console.log(nota_alumnos);

// Quitando el ultimo elemento
nota_alumnos.pop();
nota_alumnos.pop();
nota_alumnos.pop();
console.log(nota_alumnos);

//           0         1        2       3        4         5       6          7
let lista = ["Carlos", "Maria", "Jose", "Lucia", "Gaston", "Luis", "Roberto", "Mauro"];
// for "clasico"
for(i = 0; i < lista.length; i++){
    console.log("El nombre del alumno: " + i + " es: " + lista[i]);
}

// for of
for (let nombre of lista) {
    console.log(nombre);
}
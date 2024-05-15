// Busco un elemento por ID
let titulo = document.getElementById("Titulo");

// Cambio su contenido HTML
titulo.innerHTML = "Este h1 ha sido alterado por javascript";
console.log(titulo);

// Busco una lista de elementos usando su class
let importantes = document.getElementsByClassName("importante");
console.log(importantes);

// recorro cada elemento y le aplico estilos
for (let importante of importantes) {
    importante.style.backgroundColor = "#00f";
    importante.style.color = "#fff";
    importante.style.padding = "15px";
}

// Busco otra lista de elementos por su class
let secundarios = document.getElementsByClassName("secundario");

// Los borro del DOM
let longitud = secundarios.length;

for(let i = 0; i < longitud; i++){  
    secundarios[0].remove();
}

// Busco una etiqueta
let seccion = document.getElementById("Seccion1");

// Le agrego una clase por codigo
seccion.classList.add("activo");


// usando QuerySelector
let articulo = document.querySelector("#Original");
console.log(articulo);

let parrafos = document.querySelectorAll("section .importante");
console.log(parrafos);

// Clonando estructura
let original = document.querySelector("#Original");
let contenedor = document.querySelector("#Contenedor");
let copia = original.cloneNode(true); // Deep copy: copia el elemento y todos sus hijos.

original.remove();

copia.style.backgroundColor = '#f00';
copia.querySelector("h2").innerHTML = "Articulo copiado";

// contenedor.appendChild(copia.cloneNode(true));
// contenedor.appendChild(copia.cloneNode(true));
// contenedor.appendChild(copia.cloneNode(true));

function AgregarArticulo(){
    contenedor.appendChild(copia.cloneNode(true));
}

let BotonQuitar = document.querySelector("#BotonQuitar");

console.log(BotonQuitar);

BotonQuitar.addEventListener("click", function(){
    if(contenedor.childElementCount > 0) {
        contenedor.removeChild(contenedor.lastChild);
    }
});
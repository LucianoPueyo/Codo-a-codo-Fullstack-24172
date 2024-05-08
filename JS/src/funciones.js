function saludar() {
    // cuerpo de la funcion
    console.log("Hola como estas");
}

saludar(); // ejecuto la funcion

// ejemplo promedio

function promedio() {
    let continuar = true
    let suma = 0;
    let cantidad = 0;
    
    while(continuar){
        let valor = prompt("Ingrese un numero (escriba salir para terminar)");
        
        if (valor == "salir"){
            break;
        }
    
        valor = Number.parseInt(valor);
    
        suma = suma + valor; // suma += valor;
        cantidad++;
    }
    
    let promedio = suma / cantidad;
    console.log(promedio);
}

// ejemplo IVA
let bici = 1000;
let moto = 5000;
let auto = 25000;

function calculo_iva(costo){ // las funciones peden recibir 0 o mas parametro
    return costo * 1.21; // Las funciones pueden devolver solo 1 valor
}

let precio = calculo_iva(bici);
console.log(precio);

precio =calculo_iva(moto);
console.log(precio);

precio = calculo_iva(auto);
console.log(precio);
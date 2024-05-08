// Creando una clase
class Persona {
    constructor(nombre, apellido, dni){
        // atributos
        this.nombre = nombre;
        this.apellido = apellido;
        this.dni = dni;
    }

    // metodos
    presentar() {
        return "Mi nombre es " + this.nombre + " " + this.apellido;
    }
}

let persona1 = new Persona("Carlos", "Lopez", 1234);
let persona2 = new Persona("Maria", "Del Cerro", 4578);
let persona3 = new Persona("Gaston", "Perez", 6781); // Instancio la clase Persona

console.log(persona1.nombre);
console.log(persona1.apellido);
console.log(persona1.dni);
console.log(persona1.presentar());

console.log(persona3.nombre);
console.log(persona3.apellido);
console.log(persona3.dni);
console.log(persona3.presentar());
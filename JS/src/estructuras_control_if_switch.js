let condicion = true;

if(condicion){
    console.log("La condicion es verdadera");
} else {
    console.log("La condicion es falsa");
}

let valor = 237;

switch(valor){
    case 1:
        console.log("Lunes");
        break;

    case 2:
        console.log("Martes");
        break;

    case 3:
        console.log("Miercoles");
        break;

    case 4:
        console.log("Jueves");
        break;

    case 5:
        console.log("Viernes");
        break;

    case 6:
        console.log("Sabado");
        break;

    case 7:
        console.log("Domingo");
        break;

    default:
        console.log("Ese valor no representa un dia");
        break;
}
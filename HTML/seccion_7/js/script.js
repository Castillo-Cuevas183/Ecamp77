/*console.log("Hola desde la consolola JS");*/
alert("bienvenidos a la calculadora básica");
console.log("Bienvenidos a la Calculadora Básica");
alert ("Opciones 1. Suma, 2. Resta, 3. Multiplicacion, 4. Division")
opcion= parseInt (prompt("Dame el número de la opción deseada"));
var a;
var b;

a = parseInt(prompt("Ingresa numero"));
b = parseInt(prompt ("Ingresa otro numero"));
if(a == 0 && b == 0){
    alert("Los numeros son 0, no se puede hacer operaciones")
}else { 
switch (opcion){
    case 1:
        total= suma(a,b)
        alert ("resultado de la suma es " + total);
        break;
    
    case 2: 
        total2= resta(a,b)
        alert ("resultado de la resta es " + total2);
        break;

    case 3:
        total3= multiplicacion(a,b)
        alert ("resultado de la multiplicacion es " + total3);
        break;
    
    case 4:
        total4= division(a,b)
        alert ("resultado de la division es " + total4);
        break;
    
    default:
        alert ("Opción no válida, leer correctamente las opciones")
}
}
alert ("Gracias por hacer uso de la calculadora 0077")

/*if(total4 == 0){
    alert("Operacion Vacia")
}*/

function suma(a,b){
    resultado= a + b
    return resultado
}
function resta(a,b){
    resultado = a-b;
    return resultado;
}
function multiplicacion(a,b){
    resultado = a*b;
    return resultado;
}
function division(a,b){
    if(a>b){
    resultado = a/b;
} else{
    resultado =0;
}
    return resultado;
}

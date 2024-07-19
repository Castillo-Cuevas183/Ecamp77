/*console.log("Hola desde la consolola JS");*/
alert("bienvenidos a la calculadora básica");

console.log("Bienvenidos a la Calculadora Básica");
var a;
var b;
var total;

console.log (suma);
// a = 90331;
a = parseInt(prompt("Ingresa numero"));
// b= 4233324;
b = parseInt(prompt ("Ingresa otro numero"));

total= suma(a,b)
alert ("resultado de la suma es " + total);
total2= resta(a,b)
alert ("resultado de la resta es " + total2);
total3= multiplicacion(a,b)
alert ("resultado de la multiplicacion es " + total3);
total4= division(a,b)
alert ("resultado de la division es " + total4);
alert ("Gracias por hacer uso de la calculadora 0077")
if(total4 == 0){
    alert("Operacion Vacia")
}

function suma(a,b){
    resultado= a + b
    return resultado
}
function resta(a,b){
    resultado = a-b;
    return resultado
}
function multiplicacion(a,b){
    resultado = a*b;
    return resultado
}
function division(a,b){
    if(a>b){
    resultado = a/b;
} else{
    resultado =0;
}
    return resultado;
}

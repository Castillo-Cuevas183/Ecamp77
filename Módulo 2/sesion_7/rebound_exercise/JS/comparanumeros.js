// Solicitar ingreso de los números
var num1 = parseInt(prompt("Ingresa el primer número:"));
var num2 = parseInt(prompt("Ingresa el segundo número:"));

// Comparar los números y mostrar el resultado en la consola
if (num1 > num2) {
    console.log(num1 + " es mayor que " + num2);
} else if (num1 < num2) {
    console.log(num2 + " es mayor que " + num1);
} else {
    console.log(num1 + " y " + num2 + " son iguales");
}
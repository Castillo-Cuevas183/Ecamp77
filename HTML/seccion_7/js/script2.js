

alert("bienvenidos a Cálculos en Cajas de Supermercado");
console.log("Bienvenidos a Cálculos en Cajas de Supermercado");
alert ("Opciones 1. Subtotal, 2. TotalconIVA, 3. Multiplicacion, 4. Division")
opcion= parseInt (prompt("Dame el número de la opción deseada"));

var Producto1;
var Producto2;
var PrecioP1
var PrecioP2
var descuento
iva = 1.19; // IVA del 19%

Producto1 = parseInt(prompt("Ingresa cantidad Producto1"));
PrecioP1 = parseInt(prompt("Ingresa precio Producto1"));
Producto2 = parseInt(prompt ("Ingresa cantidad Producto2"));
PrecioP2 = parseInt(prompt("Ingresa precio Producto2"));
descuento = parseInt(prompt("Ingresa descuento"));

if(Producto1 == 0 && Producto2 == 0){
    alert("Los numeros son 0, no se puede hacer operaciones")
}else { 

switch (opcion){
    case 1:
        subtotal = calculoSubtotal(Producto1, Producto2, PrecioP1, PrecioP2);
        alert ("El Subtotal es " + subtotal);
    break;
                
    case 2:
    TotalconIVA:result = calculateTotalWithIva(quantity, price, iva);
    break;
                
    case 'totalDescuentoIva':
        result = calculateTotalWithDiscountAndIva(quantity, price, discount, iva);
    break;
                
    default:
        result = 'Operación no válida';
    break;
    }
}

function calculoSubtotal(Producto1, Producto2, PrecioP1, PrecioP2) {
    resultado= (Producto1 * PrecioP1 + Producto2*PrecioP2);
        return resultado
}

function calculoTotalConIva(quantity, price, iva) {
    const subtotal = calculateSubtotal(quantity, price);
    return subtotal + (subtotal * iva);
}

function calculateTotalConDescuentoeIva(quantity, price, discount, iva) {
    const subtotal = calculateSubtotal(quantity, price);
    const discountAmount = (subtotal * discount) / 100;
    const discountedSubtotal = subtotal - discountAmount;
    return discountedSubtotal + (discountedSubtotal * iva);
}
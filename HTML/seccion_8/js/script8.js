/* 
var num_articulos = parseInt(prompt("Numero de artículos que desea comprar"))
for (var inicio=1; inicio<=num_articulos; inicio++) {
    var precio_articulo = parseInt(prompt("Dame precio de articulo" + inicio))
    var cantidad_articulo = parseInt(prompt("Dame cantidad de" + inicio))
    
    console.log("Precio de articulo"+ precio_articulo);
    console.log("Cantidad"+ cantidad_articulo);
    console.log("el subtotal es=" + calcular_subtotal(precio_articulo, cantidad_articulos));
}
*/

/*
//ciclo do While//

var numero= parseInt(prompt("Ingresa un  numero"))

*/
var numero
var x=1

do{
    console.log (x);
    x = x + 1;

}while( x < numero);


//ciclo try catch//
var numero2 = parseInt(prompt("Ingresa un numero 2"));
try{
    if(numero2 !=10 ) throw new Error("El numero no es 10")
    console.log ("la ejecucion se hizo de manera Correcta")
} catch (error){
    console.log (error.name, error.message)
}





function calcular_subtotal(precio,cantidad){
    subtotal= (precio * cantidad)*1.19;
    return subtotal
}


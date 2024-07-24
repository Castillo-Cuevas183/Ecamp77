
function Mochila( color, tamaño, numeroBolsillos, numeroCierres) {

//Propiedades
this.color= color;
this.tamaño= tamaño;
this. numeroBolsillos= numeroBolsillos;
this. numeroCierres= numeroCierres;


//metodos del objeto
this.abrir_tapa= function(){
    console.log("la tapa de la mochila está abierta");
    },
this.cerrarTapa= function(){
    console.log ("La tapa de la mochila está cerrada");
    }
};


//Accediendo las propiedades del objeto

let mochila1= new Mochila("negra", "pequeña", 2,2);
let mochila2= new Mochila("roja", "mediana", 2,2);
let mochila3= new Mochila("negra", "grande", 10,10);

//Accediendo las propiedades de las instancias

console.log(mochila1.color)
console.log(mochila2.color)
console.log(mochila3.color)

mochila2.abrir_tapa();
mochila1.cerrarTapa();
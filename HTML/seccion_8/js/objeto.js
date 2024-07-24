let mochila ={
    // Propiedades del objeto
    color: "negro", 
    tamaño: "20cm",
    numeroBolsillos: 2,
    numeroCierres: 2,
    //metodos del objeto
    abrir_tapa(){
        console.log("la tapa de la mochila está abierta");
    },
    cerrarTapa(){
        console.log ("La tapa de la mochila está cerrada");
    }
};
// Accediendo a las propiedades del Objeto
console.log (mochila.color);
console.log (mochila.tamaño);
console.log (mochila.numeroCierres)

//Accediendo a los métodos del objeto
mochila.abrir_tapa ();
mochila.cerrarTapa(); 
console.log(mochila)
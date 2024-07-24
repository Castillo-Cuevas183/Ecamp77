const titulo= document.getElementById("titulo");
const descripcion= document.getElementById("descripcion");
const botonAgregar= document.getElementById("botonAgregar");
const botonCambiar= document.getElementById("cambiarValor");

function agregarElemento() {
    //crear un nuevo elemento p 
    const nuevoparrafo = document.createElement("p");
    //añadir un texto al elemento p
    nuevoparrafo.textContent = `"este es un parrafo añadido con JavaScript"`;
    // añadir una clase al elemento p
    nuevoparrafo.classList.add("nuevo-elemento");
    // añadir el elemento p al body
    document.body.appendChild(nuevoparrafo);
}

function cambiarValor() {
    // cambiar contenido del parrafo
    descripcion.textContent = "Aqui estuvo Cristian";
    descripcion.classList.add("resaltado");
}

botonAgregar.addEventListener("click", agregarElemento);
botonCambiar.addEventListener("click", cambiarValor);

/*//cambiar el color del título al hacer click    
titulo.addEventListener("click", function() {
    titulo.style.color = "red";
}); */
$(document).ready(function() {
    // Validación básica del formulario de contacto
    $("#contactForm").on("submit", function(event) {
        event.preventDefault();
        
        let name = $("#name").val().trim();
        let email = $("#email").val().trim();
        let message = $("#message").val().trim();

        if(name === "" || email === "" || message === "") {
            alert("Por favor, complete todos los campos.");
        } else {
            alert("Mensaje enviado con éxito.");
            // Limpiar el formulario
            $(this).trigger("reset");
        }
    });

    // Interactividad 
    $(".card").click(function() {
        $(this).toggleClass("bg-info");
    });
});

//Función que me aplica el estilo a la opciòn seleccionada y quita la previamente seleccionada
function seleccionar(link) {
    var opciones = document.querySelectorAll('#links  a');
    opciones[0].className = "";
    opciones[1].className = "";
    opciones[2].className = "";
    opciones[3].className = "";
    opciones[4].className = "";
    link.className = "seleccionado";

    //Hacemos desaparecer el menu una vez que se ha seleccionado una opcion
    //en modo responsive
    var x = document.getElementById("nav");
    x.className = "";
}

//función que muestra el menu responsive
function responsiveMenu() {
    var x = document.getElementById("nav");
    if (x.className === "") {
        x.className = "responsive";
    } else {
        x.className = "";
    }
}


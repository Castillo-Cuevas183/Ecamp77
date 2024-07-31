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



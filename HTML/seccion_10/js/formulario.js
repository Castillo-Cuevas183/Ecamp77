$(document).ready(function() {
    //metodo para validar un formulario
    $("#simpleform").on("submit", function(event) {
    //evitar el envío del formulario por defecto
        event.preventDefault();

        let isValid = true;
        let errorMessage = "";
        let successMessage = ";";

    //eliminar los mensajes de error
    $(".error").remove
    $("#formMessage").empty();

    //validación del formulario
    const username = $("#username").val().trim();
    if (username === "") {  
        isValid=false;
        $("#username").after('<span class="error">El nombre de usuario es obligatorio</span>');
    } 

    // Validación del correo electrónico
    const email = $('#email').val().trim();
    if (email === '') {
        isValid = false;
        $('#email').after('<span class="error">El correo electrónico es obligatorio.</span>');
    } else {
        const emailPattern = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
        if (!emailPattern.test(email)) {
            isValid = false;
            $('#email').after('<span class="error">Ingrese un correo electrónico válido.</span>');
        }
    }

        //validacion de la contraseña
        const password = $("#password").val().trim();
        if (password === "") {
            isValid = false;
            $("#password").after('<span class="error"> La contrasena es obligatoria </span>');
        }
        if (isValid) {
            successMessage = '<p class="success"> Formulario enviado exitosamente</p>'
            $("#formMessage").html(successMessage);
        } else {
            errorMessage = '<p class="error"> Por favor corrige los errores en el formulario</p>'
            $("#formMessage").html(errorMessage);
        }

    });



});


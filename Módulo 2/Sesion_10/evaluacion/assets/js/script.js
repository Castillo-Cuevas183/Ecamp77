  $(document).ready(function() {
    $(".text-body-secondary").click(function() {
        var idBoton = $(this).attr("id"); // Obtener el id del botón clickeado
        $("#detalles" + idBoton).toggle(); // Mostrar u ocultar el contenedor correspondiente
    });

    $(".btn-close").click(function() {
        $(this).closest(".detalles").hide(); // Ocultar solo el contenedor de detalles que está siendo cerrado
    });
});

$(document).ready(function() {

//ocultar y mostrar un texto
    $('#toggleButton').click(function() {
        $("#parrafo").toggle();
    })

//metodo para cambiar de color con un evento de mouse
$("#parrafo2").mouseenter(function() {  
    $(this).css("background-color", "yelow");
    }).mouseleave(function() {  
        $(this).css("background-color","red");
});

//animar una caja
$('#animatedButton').click(function () {
$("#box").animate({
    width: "200px", 
    height: '200px'
    }, 1000);
});

});

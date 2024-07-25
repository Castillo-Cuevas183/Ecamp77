// Event listener para cargar la página cuando se carga el DOM (Document Object Model)
document.addEventListener('DOMContentLoaded', function() {
    // Mostrar/Ocultar text2 al pasar el mouse por text1
    const text1 = document.getElementById('text1');
    const text2 = document.getElementById('text2');
    
    text1.addEventListener('mouseover', function() {
        text2.classList.remove('hidden');
    });

    text1.addEventListener('mouseout', function() {
        text2.classList.add('hidden');
    });

    // Agrandar imagen al hacer clic y volver a su tamaño original al salir del clic
    const img = document.getElementById('img');
    const caja2 = document.getElementById('caja2');

    caja2.addEventListener('click', function() {
        img.classList.toggle('enlarged');
    });

    // Agrandar texto en caja3 al hacer doble clic
    const caja3 = document.getElementById('caja3');
    const caja3Text = caja3.querySelector('p');

    caja3.addEventListener('dblclick', function() {
        caja3Text.classList.toggle('enlarged');
    });
});


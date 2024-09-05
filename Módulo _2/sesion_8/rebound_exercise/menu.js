//Llamar a la función para mostrar el menú
mostrarMenu(); 


function mostrarMenu() {
    let opcion = 0;

    while (opcion !== 5) {
        // Mostrar el menú y pedir la opción al usuario
        opcion = parseInt(prompt( 
            "Seleccione una opción:\n" + 
            "1. Opción 1\n" +
            "2. Opción 2\n" +
            "3. Opción 3\n" +
            "4. Opción 4\n" +
            "5. Salir"
        ));
        // Ver opciones seleccionadas
        switch(opcion) {
            case 1:
                alert("Has seleccionado la Opción 1");
            break;
            case 2:
                console.log("Seleccionó la Opción 2");
            case 3:
                console.log("Seleccionó la Opción 3");
                alert("Has seleccionado la Opción 3");
            break;
            case 4:
                console.log("Seleccionó la Opción 4");
                alert("Has seleccionado la Opción 4");
                break;
            case 5:
                console.log("Saliendo del menú...");
                alert("Saliendo del menú...");
                break;
            default:
                console.log("Opción no válida. Por favor seleccione una opción del 1 al 5.");
                alert("Opción no válida. Por favor seleccione una opción del 1 al 5.");
            break;
            }
        }
}

alert("Bienvenidos a Comparador de Números");

    // Solicitar al usuario el ingreso de dos números
    let num1 = prompt("Ingrese el primer número:");
    let num2 = prompt("Ingrese el segundo número:");

    // Convertir las entradas de texto a números
    num1 = Number(num1);
    num2 = Number(num2);

    // Verificar que los valores ingresados sean números
    if (isNaN(num1) || isNaN(num2)) {
        alert("Por favor, ingrese valores numéricos válidos.");
    } else {
        // Comparar los números y mostrar el resultado
        if (num1 > num2) {
            alert(`Esta página dice que ${num1} es mayor que ${num2}`);
        } else if (num1 < num2) {
            alert(`Esta página dice que ${num2} es mayor que ${num1}`);
        } else {
            alert("Esta página dice que ambos números tienen el mismo valor.");
        }
    }

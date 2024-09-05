let opcion = prompt(
  "¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Metel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas"
);

//FUNCIONES

switch (opcion) {
  case "1":
    let boletas = prompt("Seleccione una opcion \n1. Ver Boletas \n2. Pagar cuentas");

    if (boletas == "1") {
      alert("Ver Boletas");
    } else if (boletas == "2") {
      alert("Usted está siendo transferido. Espere por favor...");
    }
    break;

  case "2":
    let llamadas = prompt(
      "Seleccione una opcion \n1. Problemas con la señal \n2. Problemas con las llamadas");
    let info = prompt("A continuación escriba su solicitud?");
    alert("Estimado usuario, su solicitud: " + info);
    break;
    
  case "3":
    let consulta = prompt(
      "¡Mentel tiene una oferta acorde a sus necesidades! \n Para conocer mas informacion y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamará. De lo contrario  ingrese 'NO' "
    );

    if (consulta == "SI") {
      alert("Un ejecutivo se contactará con usted");
    } else if (consulta == "NO") {
      alert("Gracias por preferir nuestros servicios");
    }

    break;
  case "4":
    let consult = prompt("A continuación  escriba su consulta")
    alert("Estimado usuario, su consulta: " + consult);
    break;
  default:
    alert("La opción ingresada no es válida. Gracias  por preferir  nuestros servicios");
    break;
}

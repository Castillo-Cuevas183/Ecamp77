let clientes = [
  { id: 1, nombre: "Roberto Hernandez", clave: "1234", saldo: 1000 },
  { id: 2, nombre: "Maria Perez", clave: "1234", saldo: 2000 },
  { id: 3, nombre: "Juan Martinez", clave: "1234", saldo: 3000 },
];

let IdCliente = prompt("Ingresa el Id del cliente");
let PasswordCliente = prompt("Ingresa la contraseña");
const login = clientes.find(
  (cliente) => cliente.id == IdCliente && cliente.clave == PasswordCliente
);

if (login) {
  alert("Bienvenido " + login.nombre);

  // Las opciones en el menú serán: Ver saldo, Realizar giro, Realizar depósito y Salir.

  while (true) {
    let option = prompt(
      "Ingresa una de las siguientes opciones: \n1. Ver saldo, \n2. Realizar giro, \n3. Realizar depósito y \n4. Salir"
    );

    switch (option) {
      case "1":
        alert("Tu saldo es de: " + login.saldo);
        break;
      case "2":
        let giro = prompt("Ingresa el monto del giro");
        login.saldo = login.saldo - parseInt(giro);
        alert("Giro realizado");
        break;
      case "3":
        let deposito = prompt("Ingresa el monto del depósito");
        login.saldo = login.saldo + parseInt(deposito);
        alert("Depósito realizado");
        break;
      case "4":
        alert("Hasta pronto");
        break;
      default:
        alert("Opción invalida");
    }
  }
} else {
  alert("No se encontro el cliente");
}

//Cada uno de los clientes de nuestro banco contará con un nombre, un identificador, una clave y un saldo en su cuenta.

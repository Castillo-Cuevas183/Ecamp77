// Crear un sistema simple para gestionar tareas, donde puedas añadir tareas, marcar tareas como completadas.

//1. debe tener un constructor que acepte el título de la tarea y una bandera que indique si está completada
// 2. Debe tener un método para marcar la tarea como completada.
// 3. debe tener un método para mostrar la información de la tarea.

class Tarea {
// Constructor que acepta el título de la tarea y una bandera que indica si está completada
    constructor(titulo, completada = false) {
        this.titulo = titulo;
        this.completada = completada;
    }

// Método para marcar la tarea como completada
    marcarComoCompletada() {
        this.completada = true;
    }

// Método para mostrar la información de la tarea
    mostrarInformacion() {
        const estado = this.completada ? "Completada" : "No completada";
        console.log(`Título: ${this.titulo}, Estado: ${estado}`);
    }
}

// Crear algunas tareas de ejemplo
const tarea1 = new Tarea("Aprender JavaScript");
const tarea2 = new Tarea("Hacer ejercicios de programación");

// Mostrar la información de las tareas
tarea1.mostrarInformacion(); // Título: Aprender JavaScript, Estado: No completada
tarea2.mostrarInformacion(); // Título: Hacer ejercicios de programación, Estado: No completada

// Marcar la primera tarea como completada
tarea1.marcarComoCompletada();

// Mostrar la información de las tareas nuevamente
tarea1.mostrarInformacion(); // Título: Aprender JavaScript, Estado: Completada
tarea2.mostrarInformacion(); // Título: Hacer ejercicios de programación, Estado: No completada

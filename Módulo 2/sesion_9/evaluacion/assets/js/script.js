
// Datos iniciales
var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
];

// Función para renderizar la lista de tareas
function renderizarTareas() {
    const cuerpoTabla = document.getElementById('cuerpo-tabla'); //Obtiene una referencia al elemento del DOM con el id cuerpo-tabla, que es el cuerpo de la tabla donde se mostrarán las tareas.
    cuerpoTabla.innerHTML = ''; // Limpiar contenido previo

    tareas.forEach((item, index) => {    // Iterar sobre cada elemento del array de tareas
        const fila = document.createElement('tr'); // Crear una fila en la tabla
        
        const celdaTarea = document.createElement('td'); // Crear una celda en la fila para la tarea
        celdaTarea.textContent = item.tarea; // Crear una el elemento de las tareas del array
        fila.appendChild(celdaTarea); // Crear el elemento de la tarea 
        
        const celdaBoton = document.createElement('td'); // Crear una celda en la fila para el botón de eliminar
        const botonEliminar = document.createElement('button'); // Crear un botón para eliminar la tarea
        botonEliminar.textContent = 'Finalizar';
        botonEliminar.classList.add('btn', 'btn-danger');
        botonEliminar.onclick = function() {
            eliminarTarea(index);
        };
        celdaBoton.appendChild(botonEliminar);
        fila.appendChild(celdaBoton);
        
        cuerpoTabla.appendChild(fila);
    });
}

// Función para eliminar una tarea
function eliminarTarea(index) {
    tareas.splice(index, 1);
    renderizarTareas();
}

// Mostrar/ocultar el formulario al hacer clic en el botón "Agregar tarea"
document.querySelector('.btn-success').addEventListener('click', function() {
    const formulario = document.getElementById('formulario');
    formulario.style.display = formulario.style.display === 'none' ? 'block' : 'none';
});

// Agregar una nueva tarea
document.querySelector('.btn-primary').addEventListener('click', function() {
    const nuevaTareaInput = document.getElementById('nuevaTarea');
    const nuevaTarea = nuevaTareaInput.value.trim();
    
    if (nuevaTarea) {
        tareas.push({ tarea: nuevaTarea });
        nuevaTareaInput.value = ''; // Limpiar el campo de entrada
        renderizarTareas();
        document.getElementById('formulario').style.display = 'none'; // Ocultar el formulario
    }
});

// Inicializar la lista de tareas al cargar la página
document.addEventListener('DOMContentLoaded', renderizarTareas);


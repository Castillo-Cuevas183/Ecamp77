



function agregarTarea() {
    const tareaInput = document.getElementById('nueva-tarea');
    const tareaTexto = tareaInput.value.trim();

    if (tareaTexto === '') {
        alert('Por favor, ingrese una tarea.');
        return;
    }

    const listaTareas = document.getElementById('lista-tareas');
    const nuevaTarea = document.createElement('li');
    nuevaTarea.textContent = tareaTexto;

    const botonEliminar = document.createElement('button');
    botonEliminar.textContent = 'Eliminar';
    botonEliminar.addEventListener('click', () => {
        listaTareas.removeChild(nuevaTarea);
    });

    nuevaTarea.appendChild(botonEliminar);
    nuevaTarea.addEventListener('click', () => {
        nuevaTarea.classList.toggle('completed');
    });

    listaTareas.appendChild(nuevaTarea);
    tareaInput.value = '';
}



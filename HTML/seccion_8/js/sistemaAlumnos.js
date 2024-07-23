  // Datos de ejemplo
        const alumnos = [
            { id: 1, nombre: 'Roberto Hernandez', calificacion: 6 },
            { id: 2, nombre: 'Maria Perez', calificacion: 3 },
            { id: 3, nombre: 'Juan Martinez', calificacion: 5 }
        ];

        // Función para mostrar el menú
        function mostrarMenu() {
            console.log("Menú:");
            console.log("1. Ver lista de alumnos");
            console.log("2. Ver calificaciones de alumnos");
            console.log("3. Calcular el promedio del grupo");
            console.log("4. Salir");
        }

        // Función para ver la lista de alumnos
        function verListaAlumnos() {
            console.log("Lista de alumnos:");
            alumnos.forEach(alumno => {
                console.log(`No. ${alumno.id} Nombre: ${alumno.nombre}`);
            });
        }

        // Función para ver las calificaciones de los alumnos
        function verCalificacionesAlumnos() {
            console.log("Calificaciones de alumnos:");
            alumnos.forEach(alumno => {
                const estado = alumno.calificacion >= 4 ? 'Aprobado' : 'Reprobado';
                console.log(`Nombre: ${alumno.nombre}, Calificación: ${alumno.calificacion}, ${estado}`);
            });
        }

        // Función para calcular el promedio del grupo
        function calcularPromedioGrupo() {
            const sumaCalificaciones = alumnos.reduce((sum, alumno) => sum + alumno.calificacion, 0);
            const promedio = sumaCalificaciones / alumnos.length;
            console.log(`El promedio del grupo es: ${promedio.toFixed(1)}`);
        }

        // Función para manejar la opción seleccionada
        function manejarOpcion(opcion) {
            switch(opcion) {
                case '1':
                    verListaAlumnos();
                    break;
                case '2':
                    verCalificacionesAlumnos();
                    break;
                case '3':
                    calcularPromedioGrupo();
                    break;
                case '4':
                    console.log("Saliendo...");
                    break;
                default:
                    console.log("Opción no válida, por favor seleccione una opción del 1 al 4.");
            }
        }

        // Función principal para iniciar el sistema
        function iniciarSistema() {
            let opcion = '';
            while (opcion !== '4') {
                mostrarMenu();
                opcion = prompt("Seleccione una opción:");
                manejarOpcion(opcion);
            }
        }

        // Iniciar el sistema
        iniciarSistema();
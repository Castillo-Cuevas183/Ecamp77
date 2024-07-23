// Datos de ejemplo
const alumnos = [
    { name: 'Jhon', grade: 76 },
    { name: 'Jane', grade: 93 },
    { name: 'Samantha', grade: 90 },
    { name: 'Michael', grade: 94 },
];

// Ordenar el arreglo en orden descendente basado en la calificación
alumnos.sort((a, b) => b.grade - a.grade);
console.log('Orden descendente:', alumnos);

// Reversar el arreglo
alumnos.reverse();
console.log('Arreglo reversado:', alumnos);

// Encontrar el primer estudiante con calificación menor a 90
const primerEstudianteMenor90 = alumnos.find(alumno => alumno.grade < 90);
console.log('Primer estudiante con calificación menor a 90:', primerEstudianteMenor90);
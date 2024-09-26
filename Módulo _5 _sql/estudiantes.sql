CREATE TABLE estudiantes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    grupo CHAR(1)
);
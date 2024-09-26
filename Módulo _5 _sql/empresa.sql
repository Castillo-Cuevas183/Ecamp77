-- Active: 1725460092916@@127.0.0.1@5432@Empresa
CREATE TABLE departamentos (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(100)
);

CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    puesto VARCHAR(100),
    salario DECIMAL(10, 2),
    fecha_contratacion DATE,
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

ALTER TABLE empleados
ADD email VARCHAR(100);

ALTER TABLE empleados
RENAME TO trabajadores;


DROP TABLE departamentos;


-- Active: 1725460092916@@127.0.0.1@5432@pacientes
-- Tabla de Pacientes
CREATE TABLE Pacientes (
  PacienteID SERIAL PRIMARY KEY,
  Nombre VARCHAR(50),
  FechaNacimiento DATE,
  Genero CHAR(1)
);
 
-- Tabla de Médicos
CREATE TABLE Medicos (
  MedicoID SERIAL PRIMARY KEY,
  Nombre VARCHAR(50),
  Especialidad VARCHAR(50)
);
 
-- Tabla de Citas
CREATE TABLE Citas (
  CitaID SERIAL PRIMARY KEY,
  PacienteID INT,
  MedicoID INT,
  FechaCita DATE,
  FOREIGN KEY (PacienteID) REFERENCES Pacientes(PacienteID),
  FOREIGN KEY (MedicoID) REFERENCES Medicos(MedicoID)
);
 
-- Tabla de Tratamientos
CREATE TABLE Tratamientos (
  TratamientoID SERIAL PRIMARY KEY,
  CitaID INT,
  Descripcion TEXT,
  Costo DECIMAL(10, 2),
  FOREIGN KEY (CitaID) REFERENCES Citas(CitaID)
);


-- Insertar Pacientes
INSERT INTO Pacientes (Nombre, FechaNacimiento, Genero) VALUES ('Juan Pérez', '1985-06-15', 'M'),
('Ana Gómez', '1990-04-22', 'F'),
('Carlos Ruiz', '1978-11-30', 'M');
-- Insertar Médicos
INSERT INTO Medicos (Nombre, Especialidad) VALUES ('Dr. Martínez', 'Cardiología'),
('Dr. Sánchez', 'Pediatría'),
('Dra. López', 'Ginecología');
-- Insertar Citas
INSERT INTO Citas (PacienteID, MedicoID, FechaCita) VALUES (1, 1, '2024-09-15'),
(2, 2, '2024-09-16'),
(3, 3, '2024-09-17');
-- Insertar Tratamientos
INSERT INTO Tratamientos (CitaID, Descripcion, Costo) VALUES (1, 'Consulta general y examen físico', 150.00),
(2, 'Revisión pediátrica y vacunas', 200.00),
(3, 'Chequeo ginecológico y ecografía', 250.00);


-- INNER JOIN Mostrar todos los pacientes con la información de su médico y el tratamiento recibido:
SELECT P.Nombre AS Paciente, M.Nombre AS Medico, T.Descripcion AS Tratamiento, T.Costo
FROM Pacientes P
INNER JOIN Citas C ON P.PacienteID = C.PacienteID
INNER JOIN Medicos M ON C.MedicoID = M.MedicoID
INNER JOIN Tratamientos T ON C.CitaID = T.CitaID;


-- LEFT JOIN Mostrar todos los pacientes y, si tienen, el tratamiento recibido y el nombre del médico:
SELECT P.Nombre AS Paciente, M.Nombre AS Medico, T.Descripcion AS Tratamiento
FROM Pacientes P 
LEFT JOIN Citas C ON P.PacienteID = C.PacienteID
LEFT JOIN Medicos M ON C.MedicoID = M.MedicoID
LEFT JOIN Tratamientos T ON C.CitaID = T.CitaID;

ri
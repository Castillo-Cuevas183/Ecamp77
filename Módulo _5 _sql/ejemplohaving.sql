-- Active: 1725460092916@@127.0.0.1@5432@ejemplo3
-- Crear tabla de categorías
CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(50)
);

-- Crear tabla de proveedores
CREATE TABLE proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre_proveedor VARCHAR(50),
    pais VARCHAR(50)
);

-- Crear tabla de productos
CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    precio DECIMAL(10, 2),
    id_categoria INT REFERENCES categorias(id_categoria),
    id_proveedor INT REFERENCES proveedores(id_proveedor)
);

-- Crear tabla de ventas
CREATE TABLE ventas (
    id_venta SERIAL PRIMARY KEY,
    id_producto INT REFERENCES productos(id_producto),
    cantidad INT,
    fecha_venta DATE
);

-- Insertar categorías
INSERT INTO categorias (nombre_categoria) VALUES 
('Pinturas'),
('Herramientas'),
('Accesorios');

-- Insertar proveedores
INSERT INTO proveedores (nombre_proveedor, pais) VALUES 
('Proveedor A', 'México'),
('Proveedor B', 'EE.UU.'),
('Proveedor C', 'Canadá');

-- Insertar productos
INSERT INTO productos (nombre, precio, id_categoria, id_proveedor) VALUES
('Pintura Blanca', 100.50, 1, 1),
('Pintura Roja', 120.00, 1, 2),
('Brocha', 15.00, 2, 3),
('Rodillo', 25.00, 2, 1),
('Cinta de enmascarar', 10.00, 3, 2);

-- Insertar ventas
INSERT INTO ventas (id_producto, cantidad, fecha_venta) VALUES
(1, 50, '2024-08-01'),
(1, 60, '2024-08-15'),
(2, 20, '2024-08-03'),
(3, 100, '2024-08-05'),
(4, 120, '2024-08-08'),
(5, 200, '2024-08-10');

-- Ejemplo 1: Productos con ventas totales superiores a 100 unidades
SELECT p.nombre, SUM(v.cantidad) AS ventas_totales
FROM productos p 
JOIN ventas v ON p.id_producto = v.id_producto
GROUP BY p.nombre
HAVING SUM(v.cantidad)> 100



-- Ejemplo 2: Categorías con ingresos superiores a $10,000
SELECT c.nombre_categoria, SUM(v.cantidad * p.precio) AS ingreso_total
FROM productos p 
JOIN ventas v ON p.id_producto = v.id_producto
JOIN categorias c ON p.id_categoria = c.id_categoria
GROUP BY c.nombre_categoria
HAVING SUM(v.cantidad * p.precio)> 10000



-- Ejemplo 3: Proveedores con más de 5 productos registrados
SELECT prov.nombre_proveedor, COUNT(p.id_producto) as productos_registrados
FROM proveedor prov
JOIN productos p on p.id_proveedor = prov.id_proveedor
GROUP BY prov.nombre_proveedor
HAVING COUNT(p.id_producto) > 1


-- Ejemplo 4: Productos con un precio promedio de ventas superior a $50
SELECT p.nombre, round(avg (p.precio),1) as precio_promedio_ventas
FROM productos p
JOIN ventas v  ON v.id_producto = p.id_producto
GROUP BY p.nombre
HAVING AVG(p.precio) > 50




-- ###EXtract
-- Extraer el año de las ventas
SELECT id_venta, fecha_venta, EXTRACT(YEAR FROM fecha_venta) as YEAR
from ventas

-- Extraer el mes de las ventas
SELECT id_venta, fecha_venta, EXTRACT(MONTH FROM fecha_venta) as MONTH
from ventas

SELECT id_venta, fecha_venta, date_part("MONTH" , fecha_venta) 
from ventas


-- Ventas realizadas en un mes específico
SELECT id_venta, fecha_venta, cantidad
FROM ventas
where EXTRACT(MONTH from fecha_venta)=8


-- Ventas realizadas en un año específico
SELECT date_part('year', fecha_venta) as anio, count(*) as total_ventas
from ventas
GROUP BY date_part ('year', fecha_venta) 
ORDER BY anio

-- Número de ventas por mes
SELECT date_part('month', fecha_venta) as mes, sum(v.cantidad *p.previo) as ingresos
from ventas v
GROUP BY date_part('month', fecha_venta)
ORDER BY mes

-- Ingresos mensuales


-- #ejemplo de case when

-- Clasificar ventas en categorías de cantidad (Alta, media, baja)
SELECT id_venta, cantidad,
    CASE
        WHEN cantidad > 100 then 'Alta'
        WHEN cantidad BETWEEN 50 AND 100 THEN 'Media'
        ELSE 'Baja '
    END as  clasificacion_cantidad
FROM ventas  


-- Ejemplo 2: Asignar descuentos según el precio del producto 10% productos caro, 5% productos medios, 1% productos baratos
SELECT nombre, precio,
    CASE
        WHEN precio > 100 then '10%'
        WHEN precio BETWEEN 50 AND 100 THEN '5%'
        ELSE '1% '
    END as descuento
FROM productos  


-- Ejemplo 3: Clasificar ventas por estación del año Invierno(6,7,8), Primavera (9,10,11), Verano (12,1,2), Otoño (3,4,5)
SELECT id_venta, fecha_venta,
    CASE 
        WHEN EXTRACT(MONTH FROM fecha_venta) IN (6,7,8) THEN 'Invierno'
        WHEN EXTRACT(MONTH FROM fecha_venta) IN (9,10,11) THEN 'Primavera'
        WHEN EXTRACT(MONTH FROM fecha_venta) IN (12,1,2) THEN 'Verano'   
        ELSE  'Otono'
    END as Estacion
FROM ventas


-- Ejemplo 4: Calcular el estado del stock de productos
SELECT nombre, cantidad,
    CASE
        WHEN cantidad <= 10 THEN 'Poco'
        WHEN cantidad BETWEEN 11 AND 50 THEN 'Moderado'
        ELSE 'Alto'
    END as estado_stock
FROM productos



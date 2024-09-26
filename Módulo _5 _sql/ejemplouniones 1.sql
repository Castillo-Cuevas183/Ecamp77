-- Active: 1725460092916@@127.0.0.1@5432@ejemplo_relaciones
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE
);

INSERT INTO customers (customer_name)
VALUES ('Alice'), ('Bob'), ('Charlie'), ('David');

INSERT INTO orders (customer_id, order_date)
VALUES 
(1, '2024-09-01'), 
(2, '2024-09-02'), 
(2, '2024-09-03'),
(3, '2024-09-04');


INSERT INTO customers (customer_name)
VALUES ('Eva'), ('Frank'), ('Grace');

INSERT INTO orders (customer_id, order_date)
VALUES 
(5, '2024-09-05'), 
(6, '2024-09-06'), 
(7, '2024-09-07'), 
(3, '2024-09-08');


-- 1 INNER JOIN: devuelve las filas que tienen coincidencia en ambas tablas
SELECT c.customer_name, o.order_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id


-- 2 FULL OUTER JOIN: devuelve todas las filas cuando hay una coincidncia en una de las tablas
SELECT c.customer_name, o.order_date
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id

-- 3 left JOIN: devuelve todas las filas de la tabla izquierda y la coincidencia de la tabla derecha
SELECT c.customer_name, o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id

-- 4 RIGHT JOIN: devuelve todas las filas de la tabla derecha y la coincidencia de la tabla izquierda
SELECT c.customer_name, o.order_date
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id

-- 5 CROSS JOIN: crea una combinación de todas las filas de las tablas
SELECT c.customer_name, o.order_date
FROM customers c    
CROSS JOIN orders o

-- 6 FULL JOIN devuelce todos los regitros de las tablas hayan o no coincidencias
SELECT c.customer_name, o.order_date
FROM customers c    
FULL JOIN orders o

-- 7. INTERSECT devuelve solo los valores que están presentes en ambas consultas
SELECT customer_id FROM customers
INTERSECT
SELECT customer_id FROM orders;

-- 8 EXCEPT 
SELECT customer_id FROM customers
EXCEPT
SELECT customer_id FROM orders;


-- 9 UNION ALL: devuelve todas las filas de las tablas sin eliminar duplicados
SELECT customer_id FROM customers
UNION ALL
SELECT customer_id FROM orders;

-- 10 PRODUCTO CARTESIANO TODAS LAS COMBINACIONES POSIBLE DE FILAS
SELECT c.customer_name , o.order_date
FROM customers c, orders o

-- UNION  combina los resultados de dos o mas consultas, eliminando los duplicados
SELECT customer_name AS name, 'Customer' as source, Null AS order_date
from customers
UNION ALL
SELECT  'Order' as name, 'Order' as source, order_date
FROM orders


-- minus devuelve las filas que están en la primera consulta pero no la segunda
SELECT customer_name 
FROM customers 
EXCEPT
SELECT customer_name 
FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id




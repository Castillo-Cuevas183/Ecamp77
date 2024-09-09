-- Active: 1725460092916@@127.0.0.1@5432@tienda2
/*Obtener  la informacion de todos lo movimiento de de stock  , con el nombre del pruducto asociado:*/
SELECT  productos.nombre, movimiento_stock.tipo_moviento as Movimiento, movimiento_stock.cantidad
FROM movimiento_stock join productos  on productos.id = movimiento_stock.product_id

/* Obtener los movimiento de stock contenga la palabra entrada */

SELECT *
FROM movimiento_stock
WHERE tipo_moviento LIKE '%entrada%'

/* Actualizar el stock de un producto aumentado en 50*/

UPDATE productos
SET stock = stock + 50
WHERE id = 1

/*Obtener la cantidad total de movimientos de stock por tipo de movimiento */

SELECT tipo_movimiento, sum(cantidad) as Total
FROM movimiento_stock
GROUP BY tipo_movimiento

-- calcula el promedio de los precios de todos los productos

SELECT AVG(precios.precio) as promedio_precio
FROM precio

-- calcular el prcio mas bajo y el mas alto de los productos

SELECT MIN(precio) as precio_minimo, MAX(precio) as precio_maximo
FROM productos 
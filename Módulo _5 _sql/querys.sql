-- Active: 1725460092916@@127.0.0.1@5432@Tienda
/* Obtener la información */
SELECT productos.nombre, movimiento_stock.tipo_movimiento; as movimiento, movimiento_stockcantidad
FROM movimiento_stock JOIN  productos on  productos.id = movimiento_stock.product_id FULL JOIN

/* Obtener los movimientos de stock que contengan la parabra entrada */

SELECT *
FROM movimiento_stock
WHERE tipo_movimiento LIKE  '%entrada'


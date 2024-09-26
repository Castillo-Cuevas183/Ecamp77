-- Active: 1725460092916@@127.0.0.1@5432@transaccion_ejemplo
CREATE TABLE cuentas (
    cuenta_id SERIAL PRIMARY KEY,
    nombre TEXT,
    saldo DECIMAL
);
 
CREATE TABLE transacciones (
    transaccion_id SERIAL PRIMARY KEY,
    desde_cuenta_id INT,
    hacia_cuenta_id INT,
    monto DECIMAL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

BEGIN;
SAVEPOINT antes_transferencia;
UPDATE cuentas
SET saldo = saldo - 300
WHERE cuenta_id = 1;
UPDATE cuentas
SET saldo = saldo + 300
WHERE cuenta_id = 2;
INSERT INTO transacciones (desde_cuenta_id, hacia_cuenta_id, monto)
VALUES (1, 2, 300);

ROLLBACK to antes_transferencia

COMMIT
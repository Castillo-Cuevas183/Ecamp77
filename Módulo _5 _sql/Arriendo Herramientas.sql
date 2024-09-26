-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.arriendo
(
    folio numeric(12) NOT NULL,
    fecha date,
    dias numeric(5),
    valordia numeric(12),
    garantia character varying(30),
    herramienta_idherramienta numeric(12),
    cliente_rut character varying(10),
    CONSTRAINT arriendo_pkey PRIMARY KEY (folio)
);

CREATE TABLE IF NOT EXISTS public.cliente
(
    rut character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nombre character varying(120) COLLATE pg_catalog."default",
    correo character varying(80) COLLATE pg_catalog."default",
    direccion character varying(120) COLLATE pg_catalog."default",
    celular character varying(15) COLLATE pg_catalog."default",
    CONSTRAINT cliente_pkey PRIMARY KEY (rut)
);

CREATE TABLE IF NOT EXISTS public.empresa
(
    rut character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nombre character varying(120) COLLATE pg_catalog."default",
    direccion character varying(120) COLLATE pg_catalog."default",
    telefono character varying(15) COLLATE pg_catalog."default",
    correo character varying(80) COLLATE pg_catalog."default",
    web character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT empresa_pkey PRIMARY KEY (rut)
);

CREATE TABLE IF NOT EXISTS public.herramienta
(
    idherramienta numeric(12) NOT NULL,
    nombre character varying(120) COLLATE pg_catalog."default",
    preciodia numeric(12),
    CONSTRAINT herramienta_pkey PRIMARY KEY (idherramienta)
);

ALTER TABLE IF EXISTS public.arriendo
    ADD FOREIGN KEY (herramienta_idherramienta)
    REFERENCES public.herramienta (idherramienta) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.arriendo
    ADD FOREIGN KEY (cliente_rut)
    REFERENCES public.cliente (rut) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;

-- 1. Inserta los datos de una empresa:
INSERT INTO public.empresa (rut, nombre, direccion, telefono, correo, web)
VALUES ('111111111', 'Empresa A', 'Calle 123', '123456789', 'contacto@empresa.com', 'www.empresa.com');

-- 2. Inserta 5 herramientas:
INSERT INTO public.herramienta (idherramienta, nombre, preciodia)
VALUES (1, 'Martillo', 500), 
    (2, 'Taladro', 1000), 
    (3, 'Sierra', 750), 
    (4, 'Llave Inglesa', 300), 
    (5, 'Destornillador', 200);

-- 3. Inserta 3 clientes:
INSERT INTO public.cliente (rut, nombre, correo, direccion, celular)
VALUES ('222222222', 'Cliente 1', 'cliente1@correo.com', 'Calle 456', '987654321'),
    ('333333333', 'Cliente 2', 'cliente2@correo.com', 'Calle 789', '876543210'),
    ('444444444', 'Cliente 3', 'cliente3@correo.com', 'Calle 012', '765432109');

-- 4. Elimina el último cliente:
DELETE FROM public.cliente
WHERE rut = '444444444';

-- 5. Elimina la primera herramienta:
DELETE FROM public.herramienta
WHERE idherramienta = 1;

-- 6. Inserta 2 arriendos para cada cliente:
INSERT INTO public.arriendo (folio, fecha, dias, valordia, garantia, herramienta_idherramienta, cliente_rut)
VALUES (1, '2024-09-01', 5, 500, '1000', 2, '222222222'),
    (2, '2024-09-02', 3, 750, '1500', 3, '222222222'),
    (3, '2024-09-03', 4, 1000, '2000', 4, '333333333'),
    (4, '2024-09-04', 2, 300, '500', 5, '333333333');

-- 7. Modifica el correo electrónico del primer cliente:
UPDATE public.cliente
SET correo = 'nuevo_correo@correo.com'
WHERE rut = '222222222';

-- 8. Lista todas las herramientas:
SELECT * FROM public.herramienta;

-- 9. Lista los arriendos del segundo cliente:
SELECT * FROM public.arriendo
WHERE cliente_rut = '333333333';

-- 10. Lista los clientes cuyo nombre contiene una 'a':
SELECT * FROM public.cliente
WHERE nombre ILIKE '%a%';

-- 11. Obtén el nombre de la segunda herramienta insertada:
SELECT nombre FROM public.herramienta
WHERE idherramienta = 2;

-- 12. Modifica los primeros 2 arriendos insertados con fecha 15/01/2020:
UPDATE public.arriendo
SET fecha = '2020-01-15'
WHERE folio IN (1, 2);

-- 13. Lista Folio, Fecha y ValorDia de los arriendos de enero de 2020:
SELECT folio, fecha, valordia FROM public.arriendo
WHERE fecha BETWEEN '2020-01-01' AND '2020-01-31';

BEGIN;


CREATE TABLE IF NOT EXISTS public.clientes
(
    id serial NOT NULL,
    nombre text,
    ap_paterno text,
    direccion text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.productos
(
    id serial NOT NULL,
    nombre text,
    descripcion text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tipo_transaciones
(
    id serial NOT NULL,
    nombre text NOT NULL,
    descripcion text,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.transaciones
(
    id serial NOT NULL,
    id_cliente integer NOT NULL,
    id_producto integer NOT NULL,
    id_tipo_transacion integer NOT NULL,
    fecha date NOT NULL,
    precio float NOT NULL,
    cantidad integer NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.transaciones
    ADD FOREIGN KEY (id_cliente)
    REFERENCES public.clientes (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.transaciones
    ADD FOREIGN KEY (id_producto)
    REFERENCES public.productos (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.transaciones
    ADD FOREIGN KEY (id_tipo_transacion)
    REFERENCES public.tipo_transaciones (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
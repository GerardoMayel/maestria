/* -- Creación de la tabla 'Cuenta' con los campos especificados en el diagrama
CREATE TABLE Cuenta (
    id_cuenta INTEGER PRIMARY KEY,          -- Clave primaria, identificador único de la cuenta
    fecha_contrato DATE,                    -- Fecha en la que se hizo el contrato de la cuenta
    fecha_ultimo_pago DATE,                 -- Fecha del último pago realizado
    numero_pagos INTEGER,                   -- Número total de pagos realizados
    estatus TEXT                            -- Estatus actual de la cuenta
);

-- Creación de la tabla 'Usuario' con los campos especificados en el diagrama
CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY,         -- Clave primaria, identificador único del usuario
    nombre TEXT,                            -- Nombre del usuario
    avatar TEXT,                            -- Campo para almacenar el avatar del usuario
    fecha_ultima_actividad DATE,            -- Fecha de la última actividad del usuario
    es_titular BOOLEAN,                     -- Indicador de si el usuario es titular de la cuenta
    id_cuenta INTEGER,                      -- Clave foránea que referencia a 'id_cuenta' de la tabla 'Cuenta'
    FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta) -- Establece la relación de la clave foránea
); */

CREATE TABLE usuario (
    id_usuario INTEGER NOT NULL PRIMARY KEY,     -- Identificador único del usuario, no nulo y clave primaria
    nombre TEXT,                                 -- Nombre del usuario
    avatar TEXT,                                 -- Avatar del usuario
    fecha_ultima_actividad DATE,                 -- Fecha de la última actividad del usuario
    es_titular INTEGER                           -- Indicador de si el usuario es titular (1) o no (0)
);

CREATE TABLE contenido (
    id_contenido INTEGER NOT NULL PRIMARY KEY,   -- Identificador único del contenido, no nulo y clave primaria
    tipo INTEGER,                                -- Tipo de contenido representado por un entero
    nombre TEXT,                                 -- Nombre del contenido
    rating TEXT,                                 -- Clasificación o rating del contenido
    duracion INTEGER                             -- Duración del contenido en minutos, representado por un entero
);

CREATE TABLE usuario_ve_contenido (
    id_usuario INTEGER NOT NULL,                 -- Identificador del usuario, no nulo
    id_contenido INTEGER NOT NULL,               -- Identificador del contenido, no nulo
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),   -- Clave foránea que referencia a la tabla usuario
    FOREIGN KEY (id_contenido) REFERENCES contenido (id_contenido) -- Clave foránea que referencia a la tabla contenido
);


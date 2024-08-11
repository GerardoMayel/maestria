-- Creación de la tabla 'Cliente'
CREATE TABLE Cliente (
    ID_Cliente SERIAL PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Apellido VARCHAR(255) NOT NULL,
    Dirección TEXT NOT NULL,
    Email VARCHAR(255) NOT NULL
);

-- Creación de la tabla 'Suscripción'
CREATE TABLE Suscripcion (
    ID_Suscripcion SERIAL PRIMARY KEY,
    Fecha_Inicio DATE NOT NULL,
    Fecha_Fin DATE,
    ID_Cliente INTEGER NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente (ID_Cliente)
);

-- Creación de la tabla 'Servicio'
CREATE TABLE Servicio (
    ID_Servicio SERIAL PRIMARY KEY,
    Tipo VARCHAR(255) NOT NULL,
    Precio NUMERIC(10, 2) NOT NULL -- asumiendo que el precio tiene 2 decimales
);

-- Creación de la tabla 'Consumo'
CREATE TABLE Consumo (
    ID_Consumo SERIAL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Datos_Consumidos INTEGER NOT NULL,
    ID_Servicio INTEGER NOT NULL,
    FOREIGN KEY (ID_Servicio) REFERENCES Servicio (ID_Servicio)
);

CREATE TABLE Cuenta (id_cuenta INTEGER PRIMARY KEY, nombre_titular TEXT, detalles_pago TEXT); -- Crea tabla Cuenta con id_cuenta como clave primaria y campos para nombre del titular y detalles de pago
CREATE TABLE Usuario (id_usuario INTEGER PRIMARY KEY, nombre_usuario TEXT, id_cuenta INTEGER, FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id_cuenta)); -- Crea tabla Usuario con id_usuario como clave primaria, nombre_usuario y una clave foránea id_cuenta que referencia a Cuenta

-- Insertar en Proveedores
INSERT INTO Proveedores (id_proveedor, nombre_compania, nombre_contacto, fecha_alta) 
VALUES (1, 'Compañía Proveedora', 'Nombre Contacto', '2024-02-05');

-- Insertar en Clientes
INSERT INTO Clientes (id_cliente, nombre_compania, nombre_contacto, direccion) 
VALUES (1, 'Compañía Cliente', 'Nombre Contacto', 'Dirección Cliente');

-- Insertar en Productos
INSERT INTO Productos (id_producto, id_proveedor, nombre, precio_unitario) 
VALUES (1, 1, 'Producto 1', 10.50);

-- Insertar en Ordenes
INSERT INTO Ordenes (id_orden, id_cliente, fecha_orden) 
VALUES (1, 1, '2024-02-05');

-- Insertar en Orden_Productos
INSERT INTO Orden_Productos (id_orden, id_producto, cantidad) 
VALUES (1, 1, 2);

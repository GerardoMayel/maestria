

/* Instrucciones:

Crea un script para realizar consultas a la base de datos. El script debe incluir por lo menos una consulta usando cada una de los distintos tipos de joins.

Entregable: Archivo con script con las consultas a las relaciones.  */

-- INNER JOIN para obtener los productos y la información del proveedor correspondiente
SELECT p.id_producto, p.nombre, p.precio_unitario, pr.nombre_compania
FROM Productos p
INNER JOIN Proveedores pr ON p.id_proveedor = pr.id_proveedor;

-- LEFT JOIN para obtener todos los clientes y sus órdenes si las tienen
SELECT c.id_cliente, c.nombre_compania, o.id_orden
FROM Clientes c
LEFT JOIN Ordenes o ON c.id_cliente = o.id_cliente;

-- RIGHT JOIN para obtener todas las órdenes y la información del cliente correspondiente (incluso si el cliente no existe en la tabla de clientes por alguna razón)
SELECT c.id_cliente, c.nombre_compania, o.id_orden
FROM Clientes c
RIGHT JOIN Ordenes o ON c.id_cliente = o.id_cliente;

-- FULL OUTER JOIN para obtener una lista de todos los productos y cualquier orden de producto asociada (esto incluirá productos sin órdenes y órdenes sin productos)
SELECT p.id_producto, p.nombre, op.id_orden, op.cantidad
FROM Productos p
FULL OUTER JOIN Orden_Productos op ON p.id_producto = op.id_producto;

-- CROSS JOIN para obtener una combinación de cada cliente con cada proveedor (esto no es comúnmente utilizado en escenarios prácticos porque puede generar un número muy grande de filas)
SELECT c.id_cliente, c.nombre_compania, pr.id_proveedor, pr.nombre_compania
FROM Clientes c
CROSS JOIN Proveedores pr;

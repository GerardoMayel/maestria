/* 
Ejercicio 5 - Proyecto 6 SQL: Delete y Update
Instrucciones:

Escribe al menos 5 sentencias en 5 tablas diferentes para modificar los datos de tu base de datos

Entregable: Archivo con script con las sentencias para modificar los datos */


-- 1. Actualizar la dirección de un cliente en la tabla `Clientes`
UPDATE Clientes
SET direccion = 'Calle del Aprendizaje 123'
WHERE id_cliente = 10;

-- 2. Eliminar un proveedor específico en la tabla `Proveedores`
DELETE FROM Proveedores
WHERE id_proveedor = 50;

-- 3. Incrementar el precio unitario de todos los productos de un proveedor en la tabla `Productos`
UPDATE Productos
SET precio_unitario = precio_unitario * 1.05 -- Incremento del 5%
WHERE id_proveedor = 25;

-- 4. Cancelar una orden en la tabla `Ordenes` si no se ha enviado todavía
DELETE FROM Ordenes
WHERE id_orden = 100 AND fecha_envio IS NULL;

-- 5. Actualizar la fecha de entrega para todas las órdenes de un cliente en la tabla `Ordenes`
UPDATE Ordenes
SET fecha_entrega = '2024-12-31'
WHERE id_cliente = 20 AND fecha_entrega > CURRENT_DATE;

-- 6. Eliminar un producto de una orden en la tabla `Orden_Productos`
DELETE FROM Orden_Productos
WHERE id_orden = 10 AND id_producto = 500;

-- 7. Actualizar la cantidad de un producto en la tabla `Orden_Productos` para una orden específica
UPDATE Orden_Productos
SET cantidad = 3 -- Nueva cantidad fija
WHERE id_orden = 5 AND id_producto = 150;

-- 8. Eliminar todas las órdenes de un cliente que se hayan realizado antes de una fecha específica
DELETE FROM Ordenes
WHERE id_cliente = 15 AND fecha_orden < '2023-01-01';

-- 9. Actualizar el nombre de contacto de un cliente en la tabla `Clientes`
UPDATE Clientes
SET nombre_contacto = 'Nuevo Contacto'
WHERE id_cliente = 30;

-- 10. Eliminar productos que no se hayan vendido en ninguna orden
DELETE FROM Productos
WHERE id_producto NOT IN (SELECT id_producto FROM Orden_Productos);

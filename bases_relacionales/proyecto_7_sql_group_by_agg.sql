/* Actividad 5 - Proyecto 7 SQL: Group by y agregación
Instrucciones:

Crea por lo menos 10 sentencias SELECT donde uses funciones de agregación en conjunto con la cláusula GROUP BY.

Entregable: Archivo con script con las consultas. */


-- 1. Contar el número total de órdenes por cliente
SELECT id_cliente, COUNT(*) AS total_ordenes
FROM Ordenes
GROUP BY id_cliente;

-- 2. Calcular el precio promedio de los productos por proveedor
SELECT id_proveedor, AVG(precio_unitario) AS precio_promedio
FROM Productos
GROUP BY id_proveedor;

-- 3. Encontrar el total de productos vendidos por producto
SELECT id_producto, SUM(cantidad) AS total_vendido
FROM Orden_Productos
GROUP BY id_producto;

-- 4. Determinar el número máximo de unidades vendidas en una sola orden por producto
SELECT id_producto, MAX(cantidad) AS max_unidades_vendidas
FROM Orden_Productos
GROUP BY id_producto;

-- 5. Calcular el ingreso total por cada orden
SELECT id_orden, SUM(precio_unitario * cantidad) AS ingreso_total
FROM Orden_Productos
JOIN Productos ON Orden_Productos.id_producto = Productos.id_producto
GROUP BY id_orden;

-- 6. Obtener la cantidad mínima de productos vendidos por cada categoría de producto
SELECT categoria, MIN(cantidad) AS min_cantidad_vendida
FROM Productos
JOIN Orden_Productos ON Productos.id_producto = Orden_Productos.id_producto
GROUP BY categoria;

-- 7. Calcular el total de ingresos generados por cliente
SELECT Ordenes.id_cliente, SUM(precio_unitario * cantidad) AS ingreso_por_cliente
FROM Ordenes
JOIN Orden_Productos ON Ordenes.id_orden = Orden_Productos.id_orden
JOIN Productos ON Orden_Productos.id_producto = Productos.id_producto
GROUP BY Ordenes.id_cliente;

-- 8. Contar el número de proveedores por país
SELECT pais, COUNT(*) AS numero_proveedores
FROM Proveedores
GROUP BY pais;

-- 9. Determinar el promedio de duración de las órdenes desde su creación hasta su entrega
SELECT id_cliente, AVG(fecha_entrega - fecha_orden) AS promedio_duracion_dias
FROM Ordenes
GROUP BY id_cliente;

-- 10. Calcular el total de ingresos generados por categoría de producto
SELECT categoria, SUM(precio_unitario * cantidad) AS ingreso_por_categoria
FROM Productos
JOIN Orden_Productos ON Productos.id_producto = Orden_Productos.id_producto
GROUP BY categoria;

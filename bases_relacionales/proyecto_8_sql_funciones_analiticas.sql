
/* Actividad 6 - Proyecto 8 SQL: Funciones analítica
Instrucciones:

Crea por lo menos 5 consultas a tu bases de datos donde uses funciones analíticas. De estas 5 consultas, por lo menos 3 deben contener una ventana dinámica.

Entregable: Archivo con script con las consultas a las relaciones. */

-- 1. Asignar un rango de ventas a cada producto dentro de cada categoría basado en el total de unidades vendidas
SELECT id_producto, categoria, SUM(cantidad) OVER (PARTITION BY categoria ORDER BY SUM(cantidad) DESC) AS total_vendido,
       RANK() OVER (PARTITION BY categoria ORDER BY SUM(cantidad) DESC) AS rango_ventas
FROM Orden_Productos
JOIN Productos ON Orden_Productos.id_producto = Productos.id_producto
GROUP BY id_producto, categoria;

-- 2. Calcular el promedio móvil de 3 días del total de ventas por día
SELECT fecha_orden, SUM(precio_unitario * cantidad) AS total_ventas_dia,
       AVG(SUM(precio_unitario * cantidad)) OVER (ORDER BY fecha_orden ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS promedio_movil_3dias
FROM Orden_Productos
JOIN Productos ON Orden_Productos.id_producto = Productos.id_producto
JOIN Ordenes ON Orden_Productos.id_orden = Ordenes.id_orden
GROUP BY fecha_orden;

-- 3. Determinar el total acumulado de ventas por cliente hasta la fecha de cada orden
SELECT id_cliente, fecha_orden, SUM(precio_unitario * cantidad) AS total_ventas,
       SUM(SUM(precio_unitario * cantidad)) OVER (PARTITION BY id_cliente ORDER BY fecha_orden) AS total_acumulado
FROM Orden_Productos
JOIN Productos ON Orden_Productos.id_producto = Productos.id_producto
JOIN Ordenes ON Orden_Productos.id_orden = Ordenes.id_orden
GROUP BY id_cliente, fecha_orden;

-- 4. Asignar un número de secuencia a cada orden por cliente basado en la fecha de la orden
SELECT id_cliente, fecha_orden, 
       ROW_NUMBER() OVER (PARTITION BY id_cliente ORDER BY fecha_orden) AS secuencia_orden
FROM Ordenes;

-- 5. Calcular la diferencia en días entre cada orden y la siguiente orden para el mismo cliente
SELECT id_cliente, fecha_orden,
       LEAD(fecha_orden, 1) OVER (PARTITION BY id_cliente ORDER BY fecha_orden) - fecha_orden AS dias_hasta_siguiente_orden
FROM Ordenes;

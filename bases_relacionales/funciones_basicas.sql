/* 
Instrucciones:

Crea por lo menos 5 consultas a tu base de datos usando por lo menos una función diferente texto y/o fechas.

Entregable: Archivo con script con las consultas */



/* Consulta para obtener el número de órdenes por cliente, con nombres de cliente en mayúsculas:
sql */

SELECT id_cliente, UPPER(nombre_compania) AS nombre_compania_mayus, COUNT(id_orden) AS total_ordenes
FROM Clientes c
JOIN Ordenes o ON c.id_cliente = o.id_cliente
GROUP BY id_cliente, nombre_compania;
/* Consulta para obtener los productos y la fecha de alta del proveedor formateada:
sql */

SELECT p.nombre, TO_CHAR(pr.fecha_alta, 'FMDay, FMDDth FMMonth, YYYY') AS fecha_alta_formateada
FROM Productos p
JOIN Proveedores pr ON p.id_proveedor = pr.id_proveedor;
/* Consulta para obtener las órdenes con un mensaje que indica si la entrega está retrasada con respecto a la fecha prevista de envío:
sql */

SELECT id_orden, 
       CASE 
           WHEN fecha_entrega > fecha_envio THEN 'Entrega retrasada' 
           ELSE 'Entrega a tiempo' 
       END AS estado_entrega
FROM Ordenes;
/* Consulta para obtener la duración en días entre la fecha de orden y la fecha de entrega:
sql */

SELECT id_orden, 
       fecha_orden, 
       fecha_entrega, 
       fecha_entrega - fecha_orden AS duracion_dias
FROM Ordenes;
/* Consulta para obtener un resumen de la mensajería utilizada para las órdenes, mostrando el mes y año de la orden, y el recuento de cada mensajería:
sql */

SELECT TO_CHAR(fecha_orden, 'FMMonth YYYY') AS mes_orden, 
       mensajeria, 
       COUNT(*) AS total_por_mensajeria
FROM Ordenes
GROUP BY TO_CHAR(fecha_orden, 'FMMonth YYYY'), mensajeria
ORDER BY TO_CHAR(fecha_orden, 'FMMonth YYYY');
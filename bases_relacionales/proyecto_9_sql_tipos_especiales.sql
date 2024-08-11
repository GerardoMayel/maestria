
/* Ejercicio 6 - Proyecto 9 SQL: Tipos especiales
Instrucciones:

Crea un script con sentencias select donde uses al menos dos sentencias que vimos en esta clase.

Entregable: Archivo con script con las consultas. */

-- 1. Consulta para seleccionar y desglosar un arreglo de números telefónicos de la tabla de clientes
SELECT id, UNNEST(telefonos) AS telefono
FROM clientes
WHERE telefonos IS NOT NULL;

-- 2. Consulta para agregar un número telefónico a la lista existente de teléfonos y seleccionarlo
-- Nota: Esta consulta presupone la existencia de la columna 'telefonos' como un arreglo
SELECT id, ARRAY_APPEND(telefonos, '32 9812 1823') AS nuevos_telefonos
FROM clientes
WHERE id = 1301;

-- 3. Consulta para seleccionar el tamaño de un arreglo de productos de un pedido específico
SELECT id_orden, ARRAY_LENGTH(productos, 1) AS cantidad_productos
FROM ordenes
WHERE id_orden = 100;

-- 4. Consulta para seleccionar una entrada específica de un objeto JSON almacenado en una columna de configuraciones
SELECT id, configuraciones -> 'tema' AS tema
FROM usuarios
WHERE configuraciones IS NOT NULL;

-- 5. Consulta para combinar dos columnas de tipo JSONB y seleccionar una clave específica
-- Nota: Esta consulta presupone la existencia de las columnas 'configuracion_usuario' y 'preferencias' como JSONB
SELECT id, (configuracion_usuario || preferencias) ->> 'idioma' AS idioma_preferido
FROM usuarios
WHERE configuracion_usuario IS NOT NULL AND preferencias IS NOT NULL;

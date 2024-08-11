# -----------------------------------------------------------------------------
# ====================== BASES DE DATOS RELACIONALES ==========================
# -----------------------------------------------------------------------------
# 
# Crea un programa en Python que llene las cinco tablas. Asegúrate de haber 
# completado la práctica de "Insert y Python" para completar esta evaluación.
#
# Escribe las instrucciones SQL necesarias para:
#   - Insertar por lo menos 50 proveedores
#   - Insertar por lo menos 50 clientes
#   - Insertar por lo menos 1000 productos repartidos aleatoriamente entre los
#     distintos proveedores. Asegurate de variar el precio unitario
#   - Insertar por lo menos 100 órdenes repartidas aleatoriamente entre los 
#     distintos clientes
#   - Agregar por lo menos 2 productos a cada órden (Insertar por lo menos 2
#     registros en la tabla orden_productos
#
# No se va a evaluar el contenido de los nombres de la compañia ni de nombres
# de contacto. Tampoco las direcciones de los clientes.
#
# Criterios de Evaluación:
#   - Ejecución correcta de las sentencias INSERT: 3 puntos
#   - Inserción de por lo menos 50 proveedores: 1 punto
#   - Inserción de por lo menos 1000 productos: 1 punto
#   - Inserción de por lo menos 50 clientes: 1 punto
#   - Inserción de por lo menos 100 órdenes: 1 punto
#   - Inserción de por lo menos 2 productos por cada orden: 1 punto
#   - Integridad referencial entre todas las tablas: 2 puntos
#
# Asegúrate de escribir sentencias SQL válidas y terminarlas con ;. Es muy
# importante que no escribas texto que no sea SQL válido, o tendrás errores al
# insertar los datos en las distintas tablas.
#
# -----------------------------------------------------------------------------
import random

# Por ejemplo, primero inserta en la tabla de proveedores:
for i in range(1, 51):  # Asegurándose de insertar al menos 50 proveedores
    print("INSERT INTO proveedores (id_proveedor, nombre_compania, nombre_contacto, fecha_alta) ")
    print("VALUES ({}, '{}', '{}', '{}');".format(i, 'Proveedor {}'.format(i), 'Contacto {}'.format(i), '2024-02-05'))

# Luego inserta en la tabla de productos:
for i in range(1, 1001):  # Asegurándose de insertar al menos 1000 productos
    id_proveedor = random.randint(1, 50)  # Suponiendo que hay 50 proveedores
    precio_unitario = round(random.uniform(0.5, 100.0), 2)  # Precio aleatorio entre 0.5 y 100.0
    print("INSERT INTO productos (id_producto, id_proveedor, nombre, precio_unitario) ")
    print("VALUES ({}, {}, '{}', {});".format(i, id_proveedor, 'Producto {}'.format(i), precio_unitario))

# Tabla de clientes
for i in range(1, 51):  # Asegurándose de insertar al menos 50 clientes
    print("INSERT INTO clientes (id_cliente, nombre_compania, nombre_contacto, direccion) ")
    print("VALUES ({}, '{}', '{}', '{}');".format(i, 'Cliente {}'.format(i), 'Contacto {}'.format(i), 'Direccion {}'.format(i)))

# Ahora inserta órdenes relacionadas a esos clientes
for i in range(1, 101):  # Asegurándose de insertar al menos 100 órdenes
    id_cliente = random.randint(1, 50)  # Suponiendo que hay 50 clientes
    print("INSERT INTO ordenes (id_orden, id_cliente, fecha_orden) ")
    print("VALUES ({}, {}, '{}');".format(i, id_cliente, '2024-02-05'))

# Por último, inserta el detalle de cada orden
for i in range(1, 101):  # Para cada una de las 100 órdenes
    for j in range(2):  # Asegurándose de insertar al menos 2 productos por orden
        id_producto = random.randint(1, 1000)  # Suponiendo que hay 1000 productos
        cantidad = random.randint(1, 10)  # Cantidad aleatoria entre 1 y 10
        print("INSERT INTO orden_productos (id_orden, id_producto, cantidad) ")
        print("VALUES ({}, {}, {});".format(i, id_producto, cantidad))

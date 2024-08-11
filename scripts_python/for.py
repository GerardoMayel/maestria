# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Al igual que la sentencia while, la sentencia for nos permite ejecutar un bloque
# de código múltiples veces. La diferencia es que la sentencia for ejecuta el 
# bloque de código para cada elemento de una colección:

# Descomenta el siguiente programa y ejecutalo:
#for letra in 'cadena de texto':
#    print('letra:', letra)

# La sentencia range() y la sentencia for están hechos para trabajar en conjunto:
#for i in range(10):
#    print('i =', i)

#for x in range(-10, 10, 2):
#    print('x =', x)

# Ten cuidado de no sobreescribir el valor de la variable de control dentro del
# bloque de código:
#for x in range(-10, 10, 2):
#    x = 0
#    print('x =', x)

# Puedes usar la sentencia else dentro de for para ejecutar un bloque de código
# cuando la colección que itera la sentencia for no se cumple:
#for i in '':
#    print('i =', i)
#else:
#    print('Cadena vacia')
#############################################################################
# Iterar sobre cada carácter en una cadena de texto
for letra in 'cadena de texto':
    print('letra:', letra)

# Uso de range() con for
for i in range(10):
    print('i =', i)

# Uso de range() con valores de inicio, fin y paso
for x in range(-10, 10, 2):
    print('x =', x)

# Demostración del efecto de modificar la variable de control dentro del bucle for
for x in range(-10, 10, 2):
    x = 0
    print('x =', x)

# Uso de else con for en una colección vacía
for i in '':
    print('i =', i)
else:
    print('Cadena vacia')


# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Como vimos en la práctica pasada, el número de espacios en blanco identifican
# el nivel de bloque de código en el que se encuentra la ejecución del programa

# Ejecuta el siguiente programa.
numero = 15 # Este es el nivel "cero". No hay espacios antes de la declaración
if numero > 0:
    print('número positivo') # Nivel 1. Le indica al intérprete que esta línea
                             # de código es el bloque de la condición IF
    if numero > 10:          # Este IF sigue dentro del nivel 1.
        print('número mayor a 10') # Segundo nivel de código. Esta línea es
                                   # el bloque de código del segundo if
        if numero > 20:            # Seguimos en el segundo nivel de código
            print('número mayor a 20') # Este es bloque de tercer nivel
        print('Esto se ejecuta siempre que el número sea mayor a 10')
        # La línea anterior rgresa al segundo nivel de código
    print('Regreso a número positivo') # Y esta línea regresa al primer nivel
print('Numero =', numero)

# Modifica la variable número y ejecuta varias veces el programa

# Por defecto el número máximo de bloques de código que puedes anidar, es decir
# bloques de código dentro de otro bloque de código es de veinte (20). Este
# número se puede modificar si se recompila el intérprete de Python, aunque
# no es para nada recomendable hacer esto, ya que el funcionamiento interno
# del intérprete no está optimizado para mantener en memoria múltiples bloques
# de código anidados.

# De hecho, una buena práctica de programación es no anidar más de 3 niveles
# de código... 4 si en verdad es necesario. Una forma fácil de reducir el
# número de bloques de código anidados es usar funciones. Al final de esta
# clase sabrás crear tus propias funciones.

# Vuelve a escribir el programa anterior, pero ahora usando dos espacios
# como identificador de nivel de bloque.

# ------------------------------------------------------------------------------
# =============================== IEXE tec =====================================
# ------------------------------------------------------------------------------

# Crea dos listas siguiendo las instrucciones que acontinuación se describen.
# Es importante que uses comprensión de listas.

# Crea una lista que contenga los números múltiplos de 3 o los números multiplos
# de 5 entre el 1000 y 0, en orden descendente. 
# Por ejemplo, el 325 es mútiplo de 5, por lo que debe de estar en la lista. el 
# 936 es múltiplo de 3, por lo que debe de ir en la lista. De igual forma el 
# 675 es múltiplo de 3 y de 5, por lo que debe de estar en la lista.
#

# Crea una lista que contenga los números múltiplos de 3 o los números múltiplos
# de 5 entre el 1000 y 0, en orden descendente.
lista1 = [i for i in range(1000, -1, -1) if i % 3 == 0 or i % 5 == 0]

# Crea una lista que contenga las palabras "fizz" y "buzz" en base a la lista anterior.
# Si el número es múltiplo de 3 entonces agrega la palabra "fizz" y
# si el número es múltiplo de 5 entonces agrega la palabra "buzz".
# Si el número es múltiplo de 3 Y de 5, agrega la palabra "fizzbuzz".
lista2 = ["fizzbuzz" if i % 3 == 0 and i % 5 == 0 else "fizz" if i % 3 == 0 else "buzz" for i in lista1]

# Mostrar las primeras 10 entradas de cada lista para verificar
print("Primeros 10 elementos de lista1:", lista1[:10])
print("Primeros 10 elementos de lista2:", lista2[:10])


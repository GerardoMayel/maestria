# ------------------------------------------------------------------------------
# =============================== IEXE tec =====================================
# ------------------------------------------------------------------------------

# Crea dos diccionarios siguiendo las instrucciones que acontinuación se 
# describen. Es importante que uses comprensión de diccionarios y no modificar
# el nombre de las variables.
# 
# La comprensión de diccionarios tiene la sintaxis
# diccionario = {llave:valor for llave, valor in ...}
# Consulta este foro si tienes dudas de cómo agregar condicionales en una
# comprensión de diccionarios:
# https://stackoverflow.com/questions/9442724/how-can-i-use-if-else-in-a-dictionary-comprehension
#
# ------------------------------------------------------------------------------
# 1: crea un diccionario con los números del 1 al 100000 (cien mil). La llave 
# es el número y si es par entonces el valor es la mitad del número, y si es
# impar entonces el valor es es tres veces el valor más uno. 
#
# Por ejemplo, el diccionario con los primeros cinco números es:
# {1:4, 2:1, 3:10, 4:2, 5:16}
#
# Conoce más de la conjetura de Collatz: 
# https://en.wikipedia.org/wiki/Collatz_conjecture

# Modifica esta línea para crear el diccionario esperado.
# Recuerda no modificar el nombre de la variable para que el programa se pueda
# evaluar.

# Creación del diccionario 'collatz' usando comprensión de diccionarios
collatz = {n: n // 2 if n % 2 == 0 else 3 * n + 1 for n in range(1, 100001)}
print(collatz)
# ------------------------------------------------------------------------------
# 2: Filtra el diccionario del punto anterior con los elementos del diccionario 
# cuya llave es un número primo. Puedes usar la función descrita debajo para  
# saber si un número es primo.
# 
# Por ejemplo, para el diccionario con los primeros cinco números:
# {1:4, 2:1, 3:10, 4:2, 5:16} el diccionario resultante es: {2: 1, 3: 10, 5: 16}
# ya que 2, 3 y 5 son números primos.

def es_primo(x):
    """ Devuelve True si x es un número primo, False si no es primo. """
    if x < 2: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

collatz_primes = {k: v for k, v in collatz.items() if es_primo(k)} # Modifica esta línea para crear el diccionario esperado.
# Recuerda no modificar el nombre de la variable para que el programa se pueda
# evaluar.
#print(collatz_primes)

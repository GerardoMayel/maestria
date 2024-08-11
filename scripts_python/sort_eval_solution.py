# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

import random

ordenada = [] # Esta lista va a guardar los números y en esta misma lista se 
# van a ordenar

for i in range(1000):  # Generamos los 1000 números aleatorios
    ordenada.append(random.randint(-1000, 1000))

# Se necesitan dos ciclos. El ciclo externo recorre la lista desde el inicio
# hasta un elemento antes de que termine la lista.
for i in range(len(ordenada) - 1):
    # El ciclo anidado es igual al ciclo externo. Evalúa cada elemento de la
    # lista ordenada[j] con el elemento contiguo ordenada[j + 1]
    for j in range(len(ordenada) - 1):
        if ordenada[j] > ordenada[j + 1]: # Si el elemento actual es mayor
            # al elemento contiguo, entonces se invierten ambos valores, de
            # tal forma que el elemento de menor valor queda antes del de
            # mayor valor. Para eso necesitamos una variable temporal para 
            temp = ordenada[j + 1] # almacenar el valor y no perderlo.
            ordenada[j + 1] = ordenada[j]
            ordenada[j] = temp

print(ordenada)

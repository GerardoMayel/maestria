# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Utiliza la biblioteca random para generar 1000 números aleatorios entre -1000
# y 1000. Posteriormente ordénalos de forma ascendente. Guarda la lista final en
# una variable llamada "ordenada".

# TIP: Para ordenar la lista necesitas dos ciclos. NO USES LA FUNCIÓN 
# sort() O sorted().

import random

# Llenar la lista con 1000 elementos aleatorios
ordenada = [random.randint(-1000, 1000) for _ in range(1000)]

# Ordenar la lista usando ordenamiento por burbuja
for i in range(len(ordenada)):
    for j in range(0, len(ordenada) - i - 1):
        if ordenada[j] > ordenada[j + 1]:
            ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]


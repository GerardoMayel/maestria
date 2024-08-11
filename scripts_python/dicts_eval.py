# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Crea un diccionario con 1000 elementos, cuya llaves son los primeros 1000 
# números naturales (1, 2, 3, 4, 5, 6, 10, ..., 1000). Y el valor de cada llave
# es la cadena de texto de la llave: dict1 = {1: '1', 2: '2', 3: '3', ...}
# Crear el diccionario dict1
dict1 = {i: str(i) for i in range(1, 1001)}

# Escribe un programa en python que combine dos diccionarios en un diccionario d3
d1 = {'A': -9, 'B': 23, 'D': -19, 'E': 4, 'F': -10, 'G': -47, 'H': -18, 'M': -46, 'P': -48, 'Q': -42, 'R': 43, 'S': -31, 'T': -44, 'U': -34, 'X': 47, 'Y': 32}
d2 = {'B': -27, 'C': 27, 'D': 47, 'E': 25, 'H': 24, 'I': -17, 'K': -26, 'M': 13, 'N': 34, 'P': -24, 'T': -10, 'V': 40, 'W': -32, 'X': 36, 'Y': -21, 'Z': 19}

d3 = d1.copy()  # Copiar d1 en d3
# Sumar los valores de las llaves comunes y agregar las llaves únicas de d2
for key, value in d2.items():
    if key in d3:
        d3[key] += value
    else:
        d3[key] = value


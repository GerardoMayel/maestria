# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# En esta práctica vas a usar algunos métodos de las listas para manipular su
# contenido. Es importante que no elimines las sentencias print() para la 
# evaluacion automática.

# Escribe el código para agregar "equitación" a la tercera posición (es decir, 
# justo antes del voleibol) en la lista de deportes.
# Agregar "equitación" a la tercera posición en la lista de deportes.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, 'equitación')
print(','.join(sports)) # No modifiques esta línea

# ------------------------------------------------------------------------------
# Sacar "Londres" de la lista de viajes.
viajes = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Londres', 'Melbourne']
viajes.remove('Londres')
print(','.join(viajes)) # No modifiques esta línea

# ------------------------------------------------------------------------------
# Convertir palabras en pasado y guardar en past_verbs.
verbs = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_verbs = [verb + 'ed' for verb in verbs]
print(','.join(past_verbs)) # No modifiques esta línea

# ------------------------------------------------------------------------------
# Unir las listas A y B en una lista C.
A = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
B = ['Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
C = A + B
print(','.join(C)) # No modifiques esta línea

# ------------------------------------------------------------------------------
# Eliminar elementos de índices pares de la lista.
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Al eliminar un elemento, los índices de los elementos siguientes cambian.
# Para manejar esto, se elimina el primer elemento de los restantes en cada iteración.
for i in range(0, len(lista), 2):
    del lista[0]
print(','.join([str(c) for c in lista])) # No modifiques esta línea



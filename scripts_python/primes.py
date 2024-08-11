# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Escribe un programa que reciba un número entero del usuario y cuente la cantidad
# de números primos entre 2 y el número que ingresó el usuario. Por ejemplo:

# entrada: 1
# imprime: 0
# No hay números primos menores a 1

# entrada: 10
# imprime: "4"
# Ya que los números primos entre 2 y 10 son 2, 3, 5 y 7.

# entrada: 100
# imprime: "25"
# Ya que los números primos entre 2 y 10 son 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
# 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97.

# Un número primo es aquel que sólo es divisible entre sí mismo y uno. El número
# uno no es un número primo. Por ejemplo, 6 no es un número primo por que es 
# divisible entre 2 y 3 además de 1 y 6. Por otro lado, el número 7 sí es un
# número primo por que sólo es divisible entre 1 y 7 (si mismo).

# Tip: Vas a necesitar dos ciclos anidados, uno que cuente del 2 al número que
# ingresó el usuario, y un ciclo interno que verifique que sólo sea divisible
# entre él mismo.

n = int(input("Ingresa un número entero: "))
total_primos = 0

for i in range(2, n + 1):
    es_primo = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        total_primos += 1

print(total_primos)


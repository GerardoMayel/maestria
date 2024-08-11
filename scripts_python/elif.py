# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# En la práctica pasada vimos un ejemplo de cómo validar el usuario y contraseña
# de un usuario. Nota que este es sólo un ejemplo del uso de la sentencia if
# y para nada es como sucede en una aplicación real.
usuario = input('Cuál es tu usuario? ')
password = input('Cuál es tu contraseña? ')
if usuario == 'master' and password == 's3cr3t':
    print('Acceso correcto')
else:
    if usuario == 'root' and password == 's3cur3':
        print('Acceso correcto')
    else:
        if usuario == 'admin' and password == 'crypto':
            print('Acceso correcto')
        else:
            if usuario == 'principal' and password == 'ir0n':
                print('Acceso correcto')
            else:
                print('Usuario inválido')

# En este ejemplo, por cada usuario creamos un bloque if-else dentro del bloque
# else de la validación anterior. El nivel de bloque de código se incrementa
# en cada comparación de usuario y password.

# Una forma más clara de escribir este tipo de comparaciones múltiples es
# mediante la sentencia elif. Como su nombre sugiere, elif es una sentencia if
# dentro de una sentencia else:
num = 10
if num < 0:
    print('num es negativo')
elif num > 0:
    print('num es positivo')
else:
    print('num es cero')

# A diferencia de la sentencia else, La sentencia elif espera una comparación 
# inmediatamente después de la palabra reservada elif.
if usuario == 'master' and password == 's3cr3t':
    print('Acceso correcto')
elif usuario == 'root' and password == 's3cur3':
    print('Acceso correcto')
elif usuario == 'admin' and password == 'crypto':
    print('Acceso correcto')
elif usuario == 'principal' and password == 'ir0n':
    print('Acceso correcto')
else:
    print('Usuario inválido')

# Nota cómo después de la sentencia elif puedes usar la sentencia else.
# Después de la sentencia else no puedes usar elif:

Descomenta las siguientes líneas y ejecuta el programa.
if num < 0:
   print('num es negativo')
else:
   print('Num es mayor o igual a cero')
elif:
   print('Esto es un error')

# El mensaje de error es el siguiente:
#   File "elif.py", line 60
#     elif:
#     ^
# SyntaxError: invalid syntax

# El intérprete nos dice que hay un error de sintáxis en el la sentencia elif.

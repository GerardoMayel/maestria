# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# La sentencia IF evalúa una condición, y si el resultado es verdadero entonces
# ejecuta el bloque de código inmediato. Si la condición no es verdadera 
# entonces el intérprete omite el bloque de código inmediato a la sentencia
# if y continúa la ejecución del programa.

# Ejecuta el siguiente programa
if True:
    print('Esto siempre se va a desplegar')

if False:
    print('Esto nunca se va a desplegar')

# ------------------------------------------------------------------------------
# Ahora hagamos un ejemplo con una condición:
edad = int(input('Cuál es tu edad? '))
if edad < 18:
    anios = 18 - edad    # Los bloques de código pueden tener más una línea
    mensaje = 'Te faltan ' + str(anios) + ' años para poder votar'
    print(mensaje)
# Nota que el bloque de código del if puede tener más de una línea
# Comenta o elimina las líneas de código anteriores.

# ------------------------------------------------------------------------------
# En la condición puedes usar cualquier operador de comparación o lógico
# que evalúe a un valor booleano:
usuario = input('Cuál es tu usuario? ')
password = input('Cuál es tu contraseña? ')

if usuario == 'master' and password == 's3cr3t':
    print('Acceso correcto')
else:
    print('Acceso denegado')

# En el programa anterior usamos la sentencia ELSE. Como vimos en la clase
# la sentencia else define el bloque de código que se va a ejecutar cuando
# no se cumpla la condición del if.

if not False:
    print('no falso es verdadero')
else:
    print('no falso es falso')

# Dentro de un bloque de código IF o ELSE puedes definir más bloques de
# código:
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

# ------------------------------------------------------------------------------
# Imprime la categoría "Normal", "Sobrepeso", "Obesidad" dependiendo del
# índice de masa corporal (IMC), que se calcula:
# peso en kilogramos entre la altura en cm al cuadrado

# Si el IMC está:
#   * entre 18 y 24: Normal
#   * entre 25 y 29: Sobrepeso
#   * entre 30 y 35: Obesidad

peso = float(input('¿Cuál es tu peso? '))
altura = float(input('¿Cuál es tu altura en cm? ')) / 100  # Convertimos a metros

indice_masa_corporal = peso / (altura ** 2)

if 18 <= indice_masa_corporal < 25:
    print('Normal')
elif 25 <= indice_masa_corporal < 30:
    print('Sobrepeso')
elif 30 <= indice_masa_corporal <= 35:
    print('Obesidad')
else:
    print('Fuera de las categorías comunes')



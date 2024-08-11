# debes de leer un archivo y escribir otro archivo según
# el contenido del primero. El archivo que vas a escribir se llama 
# "evaluacion.txt" y es de texto plano.
# 
# El archivo que debes leer se llama "formato.csv" y es un archivo separado por
# comas (csv) que tiene el siguiente encabezado (primera línea):
# posicion,caracter,longitud
# 
# Debes usar estos tres valores para escribir el formato de salida. 
#   - El valor en la columna "posicion" indica la posición en la que debes 
#     escrbir los datos
#   - El valor en la columna "caracter" indica el caracter que debes escribir
#   - El valor en la columna "longitud" indica la longitud o número de
#     veces que debes repetir el caracter
# Si hay alguna posición vacía debes llenarla con el caracter espacio (' ')
# 
# Por ejemplo. Si el contenido del archivo es:
# posicion,caracter,longitud
# 0,=,10
# 10,#,5
# 20,:,20
#
# En formato de tabla:
# |--------------------------------|
# | posicion | caracter | longitud |
# |----------|----------|----------|
# |    0     |     =    |    10    |
# |   10     |     #    |     5    |
# |   20     |     :    |    20    |
# |--------------------------------|
# Tu programa debe generar un archivo con el siguiente contenido:
# ==========#####     ::::::::::::::::::::
#   - De la posición 0 a la posición 10 está el signo de igual, que corresponde
#     al primer registro de la tabla. 
#   - De la posición 10 a la 15 está el símbolo hash (#), que corresponde al
#     segundo registro de la tabla.
#   - De la posición 20 a la 40 está el signo de dos puntos (:) que corresponde
#     al tercer registro de la tabla.
#   - Nota que de la posición 16 a la 20 hay espacios en blanco, ya que 
#     no hay nada definido en ese rango.
# 
# ------------------------------------------------------------------------------
# Otro ejemplo. Si el contenido del archivo es:
# posicion,caracter,longitud
# 10,A,20
# 20,B,30
# 15,C,25
#
# En formato de tabla:
# |--------------------------------|
# | posicion | caracter | longitud |
# |----------|----------|----------|
# |   10     |     A    |    20    |
# |   20     |     B    |    30    |
# |   15     |     C    |    25    |
# |--------------------------------|
# Nota que el tercer registro del formato sobreescribe parte del primero
# por lo que el contenido del archivo va a quedar así:
#           AAAAACCCCCCCCCCCCCCCCCCCCCCCCCBBBBBBBBBB
#   - Las primeras 10 posiciones son espacios en blanco por que no hay datos
#     definidos en esas posiciones
#   - de la posición 10 a la 15 está la letra A, que corresponde al primer
#     registro de la tabla. Este bloque está sobreescrito por el tercer
#     registro de la tabla.
#   - De la posición 16 a la 25 está la letra C, que corresponde a la 
#     tercera entrada de la tabla. Este registro sobreescribió los dos
#     anteriores.
#   - De la posición 26 a la 50 está la letra B. Que corresponde al segundo
#     registro de la tabla, truncado por la tercera posición.
# 
# ------------------------------------------------------------------------------
# El archivo de formato para las pruebas (no la evaluación) es el siguiente:
# posicion,caracter,longitud
# 0,A,10
# 20,B,20
# 30,C,1
# 40,D,4
# 50,E,30
#
# En formato de tabla:
# |--------------------------------|
# | posicion | caracter | longitud |
# |----------|----------|----------|
# |    0     |     A    |    10    |
# |   20     |     B    |    20    |
# |   30     |     C    |     1    |
# |   40     |     D    |     4    |
# |   50     |     E    |    30    |
# |--------------------------------|
#
# Puedes asumir que el archivo "formato.csv" siempre va a existir y va a tener
# el formato indicado. No es necesario hacer validaciones sobre este archivo.
# Recuerda que la primera línea de este archivo es el encabezado. Los datos
# empiezan en la segunda línea. 
#
# Escribe tu código en la función crea_archivo, que es la que se ejecuta
# durante la evaluación automática.

# =============================================================================
def crea_archivo():
    """ Modifica esta función para escribir el archivo según las instrucciones 
        descritas anteriormente. No cambies el nombre de esta función para que 
        el programa se pueda evaluar correctamente.
    """
    pass


# =============================================================================
# No modifiques estas líneas
if __name__ == '__main__':
    crea_archivo()

# ------------------------------------------------------------------------------
# =============================== IEXE tec =====================================
# ------------------------------------------------------------------------------

# Ahora exploremos un problema que te vas a encontrar muchas veces. El manejo
# de las codificaciones o encoding.

# Hasta ahora, los caracteres especiales que hemos escrito en los archivos son
# acentos y otros caracteres comunes, que el intérprete no tiene problemas en
# escribir.
prueba =  open('mi_archivo.txt', 'w+') # recuerdas la diferencia entre 'w+' y 'r+'?
prueba.write('áéíóúñ')
prueba.seek(0)
print('Contenido del archivo: {}'.format(prueba.readlines()))

# Si intentamos escribir caracteres no soportados el intérprete arrojará un error:
try:
    prueba.write('У мена нет машина')
except UnicodeEncodeError as uee:
    print('Error al escribir archivo. {}'.format(str(uee)))

# El error que indica es "UnicodeEncodeError: 'charmap' codec can't encode 
#          character '\u0423' in position 0: character maps to <undefined>"
# Este error indica que el sistema no pudo convertir un caracter del alfabeto
# cirílico a su representación en bytes.

# Existen varias opciones para escribir el archivo. La primera es escribir el
# texto en un archivo en modo binario, convirtiendo el texto a una cadena de
# bytes mediante el método encode. 
#
# Primero se abre el archivo en modo binario mediante el modo 'wb'
binario = open('archivo_binario.bin', 'wb')
# Luego, el texto incompatible se convierte a su representación en Unicode
# mediante la directriz "u" inmediatamente antes de declarar la cadena de texto
texto_cirilico = u'У мена нет машина'
# Finalmente, se llama al método encode en la cadena de texto para que 
# decodifique el texto a una secuenca de bytes usando la codificación UTF-8
binario.write(texto_cirilico.encode('UTF-8'))

# Sólo para comprobar, cerramos el archivo y lo abrimos en modo lectura
binario.close()
binario = open('archivo_binario.bin', 'rb')
contenido = binario.read()
print('Contenido en binario: {}'.format(contenido))
# Como puedes ver, el contenido del archivo es una secuencia de bytes. Por 
# ejemplo, "\xd0\xa3" se refiere a la secuencia de bytes en formato hexadecimal 
# D0A3. Para convertir esta cadena de bytes a su equivalente en alfabeto 
# cirílico es necesario decodificarlo usando la misma codificación que se usó 
# para convertirlo a bytes:
texto_cirilico = contenido.decode('UTF-8')
print('Contenido binario decodificado: {}'.format(texto_cirilico))
# Conoce más del método encode y decode en la documentación oficial de Python
# https://docs.python.org/3/howto/unicode.html

# =============================================================================
# Una mejor opción es usar el argumento encoding en la función "open". 
prueba = open('mi_archivo.txt', 'r+', encoding='UTF-8')
prueba.write('У мена нет машина')
prueba.seek(0)
print('Contenido leído desde archivo de texto: {}'.format(prueba.read()))

prueba.close()

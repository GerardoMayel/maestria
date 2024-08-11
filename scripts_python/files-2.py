# ------------------------------------------------------------------------------
# =============================== IEXE tec =====================================
# ------------------------------------------------------------------------------

# En esta práctica verás las operaciones básicas de escritura y lectura de 
# archivos, además explorar algunos de los diferentes modos en que puedes abrir 
# los archivos de texto. 

# Primero creamos dos variables que manejan el archivo con nombre "mi_archivo.txt"
# uno para lectura y otro para escritura. Esta es una característica peculiar
# de Python, no todos los lenguajes de programación permiten abrir el archivo
# más de una vez. 
escritura = open('mi_archivo.txt', 'wt')
# En este punto el intérprete de Python solicita al sistema operativo de la 
# computadora que cree un archivo con el nombre "mi_archivo.txt". Como se abre
# en modo de escritura de texto (wt), si el archivo existe se borrará el contenido
# del archivo al momento de abrirlo.
lectura = open('mi_archivo.txt', 'rt')
# Ahora tenemos dos variables que apuntan al mismo archivo. Uno en modo escritura
# y otro en modo de lectura. Ambas variables apuntan al inicio del archivo, la
# posición cero.

# ------------------------------------------------------------------------------
# La escritura de texto es muy simple, mediante el método write y como argumento
# la cadena de texto que se va a escribir en el archivo.
cadena = 'Esta cadena es el primer contenido del archivo.'
escritura.write(cadena)
# El sistema operativo es responsable de escribir esta cadena de texto en el
# archivo. Internamente el sistema operativo maneja un buffer o almacén de datos
# para optimizar el acceso al disco duro o medio de almnacenamiento donde se
# encuentra el archivo. En este punto el sistema operativo puede ser que no
# haya escrito los datos en el archivo, por lo que usamos el método flush del
# archivo, que le indica al sistema operativo que vacíe dicho almacen de datos
# y escriba los datos pendientes, para después explorarlo mediante la variable
# de lectura del mismo archivo.
escritura.flush()

# Una vez que se han escrito los datos en el archivo, llamamos la método readlines
# de la variable de lectura, lo que devuelve una lista con las líneas que se
# encuentran desde la posición actual de la variable -cero en este caso- hasta
# el final del archivo.
print('Primera lectura del archivo: >{}<'.format(lectura.readlines()))
# Nota que la lectura del archivo devuelve una lista de un elemento: 
#       ['Esta cadena es el primer contenido del archivo.'] 
# Esto se debe a que el método readlines busca saltos de línea en el archivo
# indicadas por el caracter "\n". Como no encuentra nunguno, la lista contiene
# sólo un elemento.

# El método tell indica la posición actual del archivo. En ambos casos las 
# variables apuntan a la misma posición:
print('Posición de escritura: {}'.format(escritura.tell()))
print('Posición de lectura: {}'.format(lectura.tell()))
# La posición 47 es la longitud de la cadena de texto que se escribió en el
# archivo:
print('Longitud de la cadena: {}'.format(len(cadena)))

# ------------------------------------------------------------------------------
# Escribimos más datos en el archivo:
cadena2 = 'Esta cadena es la segunda escritura de datos en el archivo'
escritura.write(cadena2)
escritura.flush()
# Y la lectura va a ser la misma:
print('Segunda lectura del archivo: >{}<'.format(lectura.readlines()))
# Las posiciones ahora apuntan al final del archivo, incluyendo la nueva cadena:
print('Posición actual de escritura: {}'.format(escritura.tell()))
print('Posición actual de lectura: {}'.format(lectura.tell()))

# El método seek posiciona la variable del archivo en el caracter indicado como
# argumento. Si cambiamos la posición actual de lectura a la posición 20 y 
# leemos a partir de ahí veremos el contenido del archivo desde esta posición:
lectura.seek(20)
print('Lectura a partir de la posición 20: >{}<'.format(lectura.readlines()))

# Si se cambia la posición de escritura se van a sobreescribir los datos que ya
# se encuentren en el archivo:
escritura.seek(30)
escritura.write('(esta cadena se escribe a partir del byte 30)')
escritura.flush()

# Se reinicia la posición en la variable de lectura para leer todo el contenido
# del archivo:
lectura.seek(0)
print('Nuevo contenido del archivo: >{}<'.format(lectura.readlines()))

# Finalmente, se cierran los dos archivos para liberar los recursos de hardware:
escritura.close()
lectura.close()

# =============================================================================
# Ahora veamos el modo de escritura y lectura. Como viste en la clase, el 
# símbolo "+" indica que el archivo se abre en este doble modo. De esta forma 
# no es necesario usar dos variables:
doble_modo = open('mi_archivo.txt', 'r+')
print('Lectura en doble modo: >{}<'.format(doble_modo.readlines()))

# Ahora usemos el caracter "\n" para agregar algunos saltos de línea en el
# archivo:
doble_modo.write('\nEsta es la segunda línea del contenido del archivo')
doble_modo.write('\nEsta es la tercera y última línea del contenido del archivo')
# Reiniciamos la posición para leer desde el principio:
doble_modo.seek(0)
# En este punto ya hay tres líneas en el archivo, por lo que el método
# readlines devolverá una lista con tres posiciones:
lineas = doble_modo.readlines()
# Nota que usamos la misma variable para leer y escribir en el archivo,
# esto sólo es posible cuando se abre en doble modo mediante el símbolo "+"

print('Número de líneas leídas: >{}<'.format(len(lineas)))
for idx, linea in enumerate(lineas):
    print('línea número {}: {}'.format(idx, linea))
# Cada línea contiene al final el salto de línea, por lo que se ve un
# espacio en blanco entre cada línea.

doble_modo.close()

# =============================================================================
# Finalmente, veamos el modo de escritura exclusiva. Esto es que la apertura
# del archivo va a fallar si el archivo ya existe, de esta forma puedes asegurar
# que siempre abras un archivo nuevo y no perder datos.

try:
    error = open('mi_archivo.txt', 'xt')
except FileExistsError as fee:
    print('Error al abrir archivo: {}'.format(str(fee)))

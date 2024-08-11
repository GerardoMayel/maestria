# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# veamos el uso de los espacios en los progrmas en Python.
# Los espacios en blanco son generalmente omitidos por la mayoría de los
# lenguajes de programación. Pero en Python algunos espacios en blanco tiene
# un significado especial cuando están al principio de la línea. 

# Quita el comentario (#) de la siguiente línea y ejecuta el programa. Deja
# los espacios en blanco que están al principio.

#       print('Hola')

# Hay un error en el programa:
#
#   File "spaces.py", 
#     print('Hola')
#     ^
# IndentationError: unexpected indent

# ------------------------------------------------------------------------------
# Mira el mensaje del error: "IndentationError: unexpected indent". El intérprete
# de Python no esperaba los espacios en blanco antes de la sentencia print. Sin
# embargo, sí puedes usar espacios en blanco en otros lugares del programa:

# print        (    'Hola'    )

# Python no tuvo problemas en ejecutar la sentencia, a pesar de los espacios
# en blanco entre la sentencia print y los paréntesis. Tampoco tuvo problemas
# con los espacios en blanco que están dentro de los paréntesis.

# Esto es por que los espacios al principio de la línea son significativos.
# Python usa el número de espacios al principio de una línea para identificar
# el nivel del bloque de código de la instrucción que va a ejecutar. 

# Descomenta las siguientes líneas y ejecuta el programa
dia = 1
if dia > 1:
    print('Mayor a uno')
else:
    print('Menor a uno')

# ------------------------------------------------------------------------------
# No importa si aún no conoces la sentencia if, en esta lección la conocerás 
# a fondo. Nota que la siguiente línea después de la sentencia if tiene cuatro
# espacios al principio de la línea, estos espacios le indican al intérprete
# de Python que la instrucción está en un bloque de código diferente al de
# la línea anterior.

# dia = 1 # Aquí no hay espacios en blanco. Este es el primer nivel de código
# if dia > 1: # Este if sigue estando en el mismo nivel que la línea anterior
#     print('Mayor a uno') # Los espacios en blanco indican un nivel mayor
# else: # Esta sentencia regresa al nivel absoluto
#     print('Menor a uno') # Y ahora vuelve a estar un nivel adentro

# Inmeditatamene después de la sentencia IF, el intérprete espera un nivel de 
# indentación mayor, indicando el bloque de código que se va a ejecutar si la 
# sentencia IF se cumple. En este ejemplo el bloque de código es de sólo una 
# línea, aunque puede ser de muchas más, incluso tener más bloques de código 
# internos.

# ------------------------------------------------------------------------------
# La sentencia ELSE regresa al mismo nivel de indentación del IF, ya que 
# termina o cierra el bloque de código del IF. Nota que después de la sentencia
# ELSE se vuelve a abrir otro bloque de código que puede tener muchas líneas
# o más bloques de código internos.

# Debes tener cuidado con el uso de la tecla de tabulación, ya que un espacio
# en blanco y una tabulación tienen el mismo valor para Python, pero visualmente
# son distintos.

# if dia > 1:
#  print('mayor')
# else:
# 	print('menor')

# Nota cómo el primer bloque de código, el del if, sólo tiene un espacio en
# blanco. Mientras que el bloque de código del else tiene una tabulación
# Para el intérprete de Python los dos bloques tienen el mismo nivel de indentación
# por lo que lo puede ejecutar sin problemas, aunque visualmente son distintos.

# Dependiendo del editor de texto que uses, un símbolo de tabulación se puede
# interpretar como cuatro u ocho espacios. Este valor es configurable en todos
# los editores de texto, la mayoría de los editores de código para Python 
# reemplazan el tabulador por cuatro espacios. Algunos lo reemplazan por dos
# espacios. Lo recomendable o el estándar son cuatro espacios. 

# No importa si usas cuatro, dos, ocho o incluso un espacio de código. Mientras
# mantengas la consistencia en el número de espacios en blanco Python sabrá
# ejecutar el programa. Muchos errores difíciles de encontrar son cuando no
# usas el mísmo número de espacios en los distintos bloques de código, o combinas
# tabulaciones con espacios.

# Esta característica es un poco complicada o molesta cuando comienzas a programar
# en Python, pero es algo a lo que te acostumbras muy fácilmente. 

# ------------------------------------------------------------------------------
# Dicho esto te preguntarás, ¿por qué usar espacios en blanco para identificar
# los bloques de código? Otros lengujaes de programación usan símbolos como las
# llaves ({}) o palabras resenvadas como BEGIN Y END, que hacen más claro el
# inicio y fin de bloques de código.

# Y la respuesta es, por que los programas se leen más veces de las que se
# escriben. Por ejemplo, hoy escribes un programa, la próxima semana modificas
# algo y dentro de un mes le haces un cambio mayor. Para todos los cambios
# tuviste que leer el código varias veces, y en cada cambio ejecutaste algunas
# pruebas para ver que el programa haga lo que quieres. Para entonces el código
# lo habrás leído muchas veces más de lo que lo escribiste, tal vez no lo leas
# tu, tal vez sea un compañero de equipo o tu tengas que leer el código que
# alguien más escribió.

# Los diseñadores del lenguaje de programación Python consideraron esto y 
# decidieron usar espacios en blanco, por que así le da más claridad al código.

# Por ejemplo, Java usa llaves para identificar el inicio y fin de los bloques de
# código:
# class IfStatement {
#     public static void main(String[] args) {
#         int number = 10;
#         if (number > 0) {
#             System.out.println("Positivo");
#         } else {
#         	  System.out.println("Negativo");
#         }
#     }
# }

# ------------------------------------------------------------------------------
# Nota cómo a pesar del uso de llaves, también se usan espacios en blanco para
# delimitar los bloques de código. El programa anterior en Java hace exactamente
# lo mismo que el siguiente:

# class IfStatement {
# public static void main(String[] args) {
# int number = 10;
# if (number > 0) {
# System.out.println("Positivo");
# } else {
# System.out.println("Negativo");
# }
# }
# }

# O este:

# class IfStatement {
#     public static void main(String[] args) {
# int number = 10; if (number > 0) {
#   System.out.println("Positivo");
#         } else { System.out.println("Negativo");
# }}
#         }

# En Java, los espacios en blanco son ayuda visual para quien lee el programa, 
# mientras que las llaves son para el compilador.

# La desición que tomaron los creadores de Python fue unificar el indicador 
# visual para el programador con el indicador de loa computadora. Obligándo
# al programador a hacer programas más claros y fáciles de leer.

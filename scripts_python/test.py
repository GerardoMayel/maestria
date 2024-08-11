# ==============================================================================
# ================================== IEXE Tec ==================================
#
# Escribe un programa que sume el número de vocales, consonantes, números y 
# signos de puntuación que existen en una cadena de texto. 
#
# Consideraciones:
#   - No cuentes los espacios entre las palabras
#   - Considera minusculas y mayúsculas. A y a son vocales y B y b son consonantes
#   - Considera sólo los siguientes signos de puntuación: ,.-;:_¡!¿?/
#   - No es necesario considerar caracteres especiales como la Ñ 
#   - No es necesario considerar vocales con acento como á, é, í, ó, ú
#
# Ejemplos:
# La cadena de texto "a e  i   o    u" contiene sólo 5 vocales por lo que debes
# devolver la tupla (5, 0, 0)
#
# La cadena de texto "Este es un examen de programación!" contiene
# 12 vocales, 15 consonantes y un signo de puntuación. Por lo que debes
# devolver la tupla (12, 15, 1)
# 
# La cadena "https://technically.substack.com/archive" contiene 9 vocales, 
# 25 consonantes y 6 signos de puntuación. Por lo que debes devolver la tupla
# (9, 25, 6)
#
# Para que tu programa se evalúe correctamente, sólo modifica el bloque de 
# código donde se indica. El resto del programa no lo modifiques.
# ------------------------------------------------------------------------------

def cuenta_caracteres(texto):   # No modifiques esta línea
    num_vocales = 0             # No modifiques esta línea
    num_consonantes = 0         # No modifiques esta línea
    num_signos = 0              # No modifiques esta línea

    # escribe aquí tu programa. Itera la cadena "texto" para contar el número de
    # caracteres diferentes. Usa las variables num_vocales, num_consonantes y
    # num_signos como contadores.
    
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    signos = ",.-;:_¡!¿?/"

    for char in texto:
        if char in vocales:
            num_vocales += 1
        elif char in consonantes:
            num_consonantes += 1
        elif char in signos:
            num_signos += 1

    return (num_vocales, num_consonantes, num_signos) # No modifiques esta línea


# ------------------------------------------------------------------------------
# No modifiques el resto de este programa
if __name__ == '__main__':                              # No modifiques esta línea
    test_str = input('Escribe una cadena de prueba ')   # No modifiques esta línea
    conteos = cuenta_caracteres(test_str)               # No modifiques esta línea
    print('La cadena tiene %i vocales, %i consonantes y %i signos' % conteos)  # No modifiques esta línea

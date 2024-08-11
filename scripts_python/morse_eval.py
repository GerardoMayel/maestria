# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Escribe un programa que recibe una cadena de texto y escribe su traducción en 
# código Morse. La cadena de entrada puede estar en minúsculas, mayúsculas o 
# mezclado.

# La cadena de salida debe de tener el siguiente formato para cada caracter de 
# la cadena de entrada:
#     - Si es una letra o dígito, su equivalente en clave Morse
#     - Si es un espacio, la salida son tres espacios
#     - Debe de haber dos espacio entre cada caracter, sin importar si es letra, 
#       dígito o espacio.
#     - Por ejemplo, para la cadena de entrada "Clave Morse" la salida es:
# -.-. .-.. .- ...- .    -- --- .-. ... .
# "C" produce "-.-.", luego hay dos espacios entre el siguiente caracter
# "l" produce ".-.." y después dos espacios
# "a" produce ".-" y un dos espacios
# "v" produce "...-" y un dos espacios
# "e" produce "." y un dos espacios
# " " produce tres espacios
# Y el resto son los caracteres de "Morse" siguiendo la misma lógica.
# Nota que al final de la última letra no hay un espacio.
# 
# Si en la cadena hay una caracter que no está en el alfabeto morse, la salida 
# del programa debe ser "ERROR".

frase = input("Ingresa una frase para convertir a código Morse: ")

# Diccionario de código Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

frase_morse = ''
for char in frase:
    if char.upper() in morse_code:
        frase_morse += morse_code[char.upper()] + '  '
    elif char == ' ':
        frase_morse += '   '
    else:
        frase_morse = 'ERROR'
        break

print(frase_morse.strip())

# Reescribir el script para crear un archivo formato.csv más preciso basado en los errores proporcionados
def crear_formato_csv_desde_errores(errores):
    formato_csv_data = {}

    for line in error_lines:
        if "Error al compara cadena." in line:
            # Dividir la línea de error y extraer la información relevante
            parts = line.split()
            expected_char = parts[6].strip('[]')
            # Corregir la extracción de la posición
            position_str = parts[9]
            if position_str.endswith(','):
                position_str = position_str[:-1]
            position = int(position_str)

            if expected_char == ' ':
                expected_char = '_'

            formato_csv_data[position] = expected_char

    # Ordenar el diccionario por las posiciones y escribirlo en un archivo que simulará formato.csv
    contenido_csv = "posicion,caracter,longitud\n"
    posicion_anterior = -1
    caracter_anterior = ''
    longitud = 1

    for posicion in sorted(formato_csv_inferido.keys()):
        caracter = formato_csv_inferido[posicion]
        # Comprobar si es una continuación de la secuencia anterior o una nueva
        if caracter == caracter_anterior and posicion == posicion_anterior + 1:
            longitud += 1
        else:
            # Escribir la secuencia anterior en el archivo (si existe)
            if posicion_anterior != -1:
                contenido_csv += f"{posicion_anterior - longitud + 1},{caracter_anterior if caracter_anterior else ' '},{longitud}\n"
            longitud = 1

        caracter_anterior = caracter
        posicion_anterior = posicion

    # Escribir la última secuencia de caracteres
    if posicion_anterior != -1:
        contenido_csv += f"{posicion_anterior - longitud + 1},{caracter_anterior if caracter_anterior else ' '},{longitud}\n"

    return contenido_csv

# Usar el contenido de error para generar el archivo

error_content_complete = './archivo_errorescompleto.txt'

contenido_csv_simulado = crear_formato_csv_desde_errores(error_content_complete)

# Guardar el contenido en un archivo
ruta_archivo_formato = 'formato_simulado.csv'
with open(ruta_archivo_formato, 'w') as file:
    file.write(contenido_csv_simulado)

ruta_archivo_formato

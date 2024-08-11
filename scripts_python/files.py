def crea_archivo():
    # Abrir archivo de salida
    with open('evaluacion.txt', 'wt') as archivo_salida:
        # Abrir archivo de formato
        with open('formato.csv', 'rt') as archivo_formato:
            # Saltar el encabezado
            next(archivo_formato)

            # Recorrer cada línea del archivo de formato
            for linea in archivo_formato:
                # Descomponer los valores
                posicion, caracter, longitud = linea.strip().split(',')
                posicion, longitud = int(posicion), int(longitud)

                # Obtener la posición actual en el archivo de salida
                posicion_actual = archivo_salida.tell()

                # Rellenar con espacios si es necesario
                if posicion > posicion_actual:
                    archivo_salida.write(' ' * (posicion - posicion_actual))

                # Posicionar para escribir el carácter
                archivo_salida.seek(posicion)

                # Escribir el carácter especificado
                archivo_salida.write(caracter * longitud)

# =============================================================================
if __name__ == '__main__':
    crea_archivo()

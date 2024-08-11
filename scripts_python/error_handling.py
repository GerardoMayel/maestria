# ------------------------------------------------------------------------------
# =============================== IEXE tec =====================================
# ------------------------------------------------------------------------------

# Modifica las siguientes funciones para que la función "maneja_error" llame a
# la función "peligro". La función "maneja_error" recibe como argumento una
# lista. Ejecuta el método append() sobre la lista para agregar alguno de los
# siguientes valores numéricos:
#   - 1 sin importar si ocurre una excepción o no
#   - 2 sólo si el método "peligro" arroja una excepción de tipo ValueError
#   - 3 sólo si el método "peligro" no arroja ninguna excepción

# Para que tu programa se evalúe correctamente no modifiques los nombres de 
# las funciones o variables. Y asegúrate de ejecutar el método append sobre
# la variable "lista".


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def peligro():  # No modifiques el nombre de la función
    """ Modifica esta función para hacer pruebas. Esta función no se ejecuta
        durante la evaluación automática.
    """
    pass


# ------------------------------------------------------------------------------
def maneja_error(lista):  # No modifiques el nombre ni el argumento de la función
    """ Modifica esta función para agregar a la lista el valor esperado según
        las instrucciones.
    """
    try:
        peligro()
    except ValueError as ve:
        lista.append(3)
    else:
        lista.append(2)
    finally:
        lista.append(1)








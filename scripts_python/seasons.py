# ------------------------------------------------------------------------------
# =================== Programación para Ciencia de Datos =======================
# ------------------------------------------------------------------------------

# Captura el año, mes y dia del usuario:
anio = int(input("Introduce el año (formato YYYY): "))
mes = int(input("Introduce el mes (1-12): "))
dia = int(input("Introduce el día (1-31): "))

# Validación simple del año, mes y dia
if anio <= 0 or mes <= 0 or dia <= 0:
    print('Fecha Invalida')
elif mes > 12:
    print('Fecha Invalida')
else:
    # Revisa si el año es bisiesto
    es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

    # Días máximos por mes, considerando febrero para años no bisiestos y bisiestos
    dias_por_mes = [31, 29 if es_bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dia > dias_por_mes[mes - 1]:
        print('Fecha Invalida')
    else:
        # Determinar la estación del año
        if (mes == 3 and dia >= 20) or (3 < mes < 6) or (mes == 6 and dia < 20):
            print("Primavera")
        elif (mes == 6 and dia >= 20) or (6 < mes < 9) or (mes == 9 and dia < 22):
            print("Verano")
        elif (mes == 9 and dia >= 22) or (9 < mes < 12) or (mes == 12 and dia < 21):
            print("Otoño")
        else:
            print("Invierno")

#!/bin/bash

# p2.sh

# Obtener el número correcto de columnas
columnas_correctas=$(head -n 1 profeco.csv | awk -F',' '{print NF}')

# Utilizar awk estándar para contar líneas con menos o más columnas de lo esperado
echo "Líneas con menos columnas de las esperadas:"
awk -F',' -v cols="$columnas_correctas" 'NR>1 && NF<cols' profeco.csv | wc -l

echo "Líneas con más columnas de las esperadas:"
awk -F',' -v cols="$columnas_correctas" 'NR>1 && NF>cols' profeco.csv | wc -l

# Encabezado de columnas en minúsculas
echo "Encabezado de columnas en minúsculas:"
head -n 1 profeco.csv | tr '[:upper:]' '[:lower:]'

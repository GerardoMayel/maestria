#!/bin/bash

# p1.sh

# a. Imprime cuántos registros tienes en este dataset (excluyendo el encabezado)
echo "Número de registros (excluyendo el encabezado):"
tail -n +2 profeco.csv | wc -l

# b. Imprime el nombre de las columnas que tiene tu dataset
echo "Nombres de las columnas:"
head -n 1 profeco.csv

# c. Imprime el número de columnas que tiene tu dataset
echo "Número de columnas:"
head -n 1 profeco.csv | awk -F',' '{print NF}'

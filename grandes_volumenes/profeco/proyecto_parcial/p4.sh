#!/bin/bash

# p4.sh

# Modificar la columna "DIRECCIÓN" y buscar "guadalupe"
awk -F',' 'NR>=1000 && NR<=2000 {gsub(/[.-\/]/, "", $11)} {print NR, $0}' profeco.csv | grep -i "guadalupe" > temp_guadalupe.txt

# Imprimir si no supera los 1000 registros
if [ $(wc -l < temp_guadalupe.txt) -le 1000 ]
then
    cat temp_guadalupe.txt
else
    echo "Más de 1000 registros contienen 'guadalupe', no es viable mostrar todos en pantalla."
    echo "Total de registros con 'guadalupe': $(wc -l < temp_guadalupe.txt)"
fi

rm temp_guadalupe.txt

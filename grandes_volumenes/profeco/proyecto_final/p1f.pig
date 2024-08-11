#!/bin/bash

# p1f.sh
# Elimina el encabezado del archivo y filtra por líneas con exactamente 15 columnas.

awk -F',' 'NR > 1 && NF == 15' profeco.csv > profeco_w_header.csv

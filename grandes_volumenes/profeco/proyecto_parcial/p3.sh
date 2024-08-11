#!/bin/bash

# p3.sh

# a. Productos con "fresita"
echo "Productos con 'fresita':"
grep -i "fresita" profeco.csv | head -n 11 | tail -n +2

# b. Producto y categoría de los registros específicos
echo "Producto y categoría de los registros 222222 y 333333:"
awk -F',' 'NR==222223 || NR==333334 {print $1, $4}' profeco.csv

# c. Giros con "lleria"
echo "Giros con 'lleria':"
grep -i "lleria" profeco.csv | awk -F',' '{print $9}' | head -n 10

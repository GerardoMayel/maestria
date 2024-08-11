#!/bin/bash

# ejecutar_todo.sh

echo "Ejecutando p1.sh - Información Básica del Dataset:"
#./p1.sh
echo "-------------------------------------------------"

echo "Ejecutando p2.sh - Análisis de Columnas:"
./p2.sh
echo "-------------------------------------------------"

echo "Ejecutando p3.sh - Búsquedas Específicas:"
./p3.sh
echo "-------------------------------------------------"

echo "Ejecutando p4.sh - Modificación y Filtro de Datos:"
./p4.sh
echo "-------------------------------------------------"

echo "Todos los scripts se han ejecutado."

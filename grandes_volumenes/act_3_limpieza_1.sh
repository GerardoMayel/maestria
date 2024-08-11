#!/bin/bash

# Nombre del archivo CSV
archivo="uci-news-aggregator.csv"

echo "Respuestas a las preguntas de las actividades:"
echo "------------------------------------------------"

# Pregunta 1
echo "1. ¿Cuántas noticias son publicadas por el portal de 'nasdaq'?"
cantidad_nasdaq=$(grep -i ',nasdaq,' $archivo | wc -l)
echo "Respuesta: Hay $cantidad_nasdaq noticias publicadas por el portal de 'nasdaq'."

# Pregunta 2
echo -e "\n2. ¿En qué líneas del archivo se encuentran las noticias que hablan de 'rusia'?"
lineas_rusia=$(grep -in '\brusia\b' $archivo | cut -d':' -f1 | tr '\n' ',' | sed 's/,$/\n/')
echo "Respuesta: Las noticias que hablan de 'rusia' se encuentran en las líneas:"
echo "($lineas_rusia)"

# Pregunta 3
echo -e "\n3. ¿Cuáles son los títulos de las últimas 3 noticias de reuters?"
ultimas_tres_reuters=$(grep -i ',reuters,' $archivo | tail -n 3 | cut -d',' -f2)
echo "Respuesta: Los títulos de las últimas 3 noticias de reuters son:"
echo "$ultimas_tres_reuters"

# Pregunta 4
echo -e "\n4. ¿Cuántas noticias tienen en su título tres puntos suspensivos '...'?"
cantidad_puntos=$(grep -o '\.\.\.' $archivo | wc -l)
echo "Respuesta: Hay $cantidad_puntos noticias con tres puntos suspensivos en su título."

# Pregunta 5
echo -e "\n5. ¿Cuántas noticias tienen la palabra 'CEO,' explícitamente en mayúsculas?"
cantidad_ceo=$(grep -o '\bCEO,\b' $archivo | wc -l)
echo "Respuesta: Hay $cantidad_ceo noticias con la palabra 'CEO,' en mayúsculas."

# Pregunta 6
echo -e "\n6. ¿Cuántas noticias tiene la palabra 'likely' o 'unlikely'?"
cantidad_likely_unlikely=$(grep -i -e '\blikely\b' -e '\bunlikely\b' $archivo | wc -l)
echo "Respuesta: Hay $cantidad_likely_unlikely noticias con la palabra 'likely' o 'unlikely'."

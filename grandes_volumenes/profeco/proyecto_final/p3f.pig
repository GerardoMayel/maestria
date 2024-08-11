-- p3f.pig

REGISTER '/path/to/my/udfs.jar';  -- Ajustar al path correcto

data = LOAD 'profeco_w_header.csv' USING PigStorage(',') AS (
    producto:chararray, presentacion:chararray, marca:chararray,
    categoria:chararray, catalogo:chararray, precio:double,
    fecharegistro:chararray, cadenacomercial:chararray, giro:chararray,
    nombrecomercial:chararray, direccion:chararray, estado:chararray,
    municipio:chararray, latitud:double, longitud:double
);

-- a. Diferentes categorías y número de registros
categorias_grouped = GROUP data BY categoria;
categoria_counts = FOREACH categorias_grouped GENERATE group AS categoria, COUNT(data) AS count;
categoria_sorted = ORDER categoria_counts BY count DESC;
DUMP categoria_sorted;

-- b. Estado con menor consumo de "AZUCAR"
azucar_data = FILTER data BY categoria MATCHES '.*AZUCAR.*';
estados_azucar = GROUP azucar_data BY estado;
min_consumo_azucar = FOREACH estados_azucar GENERATE group AS estado, COUNT(azucar_data) AS count;
min_estado_azucar = ORDER min_consumo_azucar BY count;
DUMP LIMIT min_estado_azucar 1;

-- c. Top 10 marcas de "HUEVO"
huevo_data = FILTER data BY categoria MATCHES '.*HUEVO.*';
marcas_huevo = GROUP huevo_data BY marca;
marca_counts = FOREACH marcas_huevo GENERATE group AS marca, COUNT(huevo_data) AS count;
sorted_marcas = ORDER marca_counts BY count DESC;
DUMP LIMIT sorted_marcas 10;

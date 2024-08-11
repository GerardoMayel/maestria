-- p2f.pig

REGISTER '/path/to/my/udfs.jar';  -- Ajustar al path correcto

data = LOAD 'profeco_w_header.csv' USING PigStorage(',') AS (
    producto:chararray, presentacion:chararray, marca:chararray, 
    categoria:chararray, catalogo:chararray, precio:double,
    fecharegistro:chararray, cadenacomercial:chararray, giro:chararray,
    nombrecomercial:chararray, direccion:chararray, estado:chararray,
    municipio:chararray, latitud:double, longitud:double
);

-- a. Diferentes giros y número de registros
giros_grouped = GROUP data BY giro;
giro_counts = FOREACH giros_grouped GENERATE group AS giro, COUNT(data) AS count;
DUMP giro_counts;

-- b. Diferentes estados y número de registros
estados_grouped = GROUP data BY estado;
estado_counts = FOREACH estados_grouped GENERATE group AS estado, COUNT(data) AS count;
DUMP estado_counts;

-- c. ¿Faltan estados?
todos_estados = FOREACH estados_grouped GENERATE group AS estado;
faltantes = FILTER todos_estados BY NOT (estado MATCHES '.*[a-zA-Z]+.*');
DUMP faltantes;

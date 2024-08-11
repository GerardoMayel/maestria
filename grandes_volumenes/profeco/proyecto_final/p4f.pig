-- p4f.pig

REGISTER '/path/to/my/udfs.jar';  -- Ajustar al path correcto

data = LOAD 'profeco_w_header.csv' USING PigStorage(',') AS (
    producto:chararray, presentacion:chararray, marca:chararray,
    categoria:chararray, catalogo:chararray, precio:double,
    fecharegistro:chararray, cadenacomercial:chararray, giro:chararray,
    nombrecomercial:chararray, direccion:chararray, estado:chararray,
    municipio:chararray, latitud:double, longitud:double
);

-- a. Precio más alto del producto "tortilla" por estado
tortilla_data = FILTER data BY producto MATCHES '.*tortilla.*';
max_price = GROUP tortilla_data BY estado;
max_price_state = FOREACH max_price GENERATE group AS estado, MAX(tortilla_data.precio) AS max_precio;
DUMP max_price_state;

-- b. Precio más bajo del producto "tortilla" por estado
min_price = GROUP tortilla_data BY estado;
min_price_state = FOREACH min_price GENERATE group AS estado, MIN(tortilla_data.precio) AS min_precio;
DUMP min_price_state;

-- c. Precio promedio del producto "tortilla" por estado
avg_price = GROUP tortilla_data BY estado;
avg_price_state = FOREACH avg_price GENERATE group AS estado, AVG(tortilla_data.precio) AS avg_precio;
DUMP avg_price_state;

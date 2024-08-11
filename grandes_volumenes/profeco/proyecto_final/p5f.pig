-- p5f.pig

REGISTER '/path/to/my/udfs.jar';  -- Ajustar al path correcto

data = LOAD 'profeco_w_header.csv' USING PigStorage(',') AS (
    producto:chararray, presentacion:chararray, marca:chararray,
    categoria:chararray, catalogo:chararray, precio:double,
    fecharegistro

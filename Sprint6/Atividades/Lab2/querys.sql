CREATE DATABASE meubanco;

CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.pessoas (
  nome STRING,
  sexo STRING,
  total INT,
  ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION "s3://pblabum/dados";

SELECT nome FROM meubanco.pessoas WHERE ano = 1999 ORDER BY total LIMIT 15;
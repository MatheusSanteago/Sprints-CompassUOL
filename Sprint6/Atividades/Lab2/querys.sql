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

WITH contador AS (
  SELECT
    CONCAT(SUBSTRING(CAST(ano AS VARCHAR), 1, 3), '0s') AS decada,
    name,
    SUM(total) AS quantidade,
    ROW_NUMBER() OVER (PARTITION BY CONCAT(SUBSTRING(CAST(ano AS VARCHAR), 1, 3), '0s') ORDER BY SUM(total) DESC) AS pos
  FROM
    meubanco.pessoas
  WHERE
    ano >= 1950 
  GROUP BY
    CONCAT(SUBSTRING(CAST(ano AS VARCHAR), 1, 3), '0s'), name
)
SELECT
  decada,
  name,
  quantidade
FROM
  contador
WHERE
  pos <= 3
ORDER BY
  decada, quantidade DESC
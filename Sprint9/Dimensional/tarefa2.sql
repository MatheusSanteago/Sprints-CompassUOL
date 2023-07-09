-------------------------------------------
--CLIENTE 

CREATE VIEW [dim_cliente] AS 
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_cliente;

SELECT * FROM [dim_cliente];

-------------------------------------------
--VENDEDOR
 
CREATE VIEW [dim_vendedor] AS 
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_vendedor;

SELECT * FROM [dim_vendedor];

-------------------------------------------
--COMBUSTIVEL 

CREATE VIEW [dim_combustivel] AS 
SELECT idCombustivel, tipoCombustivel
FROM tb_combustivel;

SELECT * FROM [dim_combustivel];

-------------------------------------------
--CARRO 

CREATE VIEW [dim_carro] AS 
SELECT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel 
FROM tb_carro tcar;

SELECT * FROM [dim_carro];
-----------------------------------------------
--KMRODADOS 


CREATE VIEW [dim_kmRodados] AS 
SELECT idLocacao, kmCarro
FROM tb_kmRodados;

SELECT * FROM [dim_kmRodados];


-----------------------------------------------
--TEMPO

CREATE VIEW [dim_tempo] AS 
SELECT 
	DATE(SUBSTRING(dataLocacao, 1,4) || '-' || SUBSTRING(dataLocacao, 5,2) || '-' || SUBSTRING(dataLocacao, 7,2)) as dataLocacao,  
	horaLocacao,
	SUBSTRING(dataLocacao, 0,5) AS AnoLocacao,
	SUBSTRING(dataLocacao, 5,2) AS MesLocacao,
	SUBSTRING(dataLocacao, 7,2) AS DiaLocacao,
	DATE(SUBSTRING(dataEntrega , 1,4) || '-' || SUBSTRING(dataEntrega, 5,2) || '-' || SUBSTRING(dataEntrega, 7,2)) as dataEntrega,
	horaEntrega,
	SUBSTRING(dataEntrega, 0,5) AS AnoEntrega,
	SUBSTRING(dataEntrega, 5,2) AS MesEntrega,
	SUBSTRING(dataEntrega, 7,2) AS DiaEntrega 
FROM tb_locacao;

SELECT * FROM [dim_tempo];

---------------------------------------------
--- FATO LOCAÇÃO
CREATE VIEW [fato_locacao] AS 
SELECT 
	idLocacao, 
	DATE(SUBSTRING(dataLocacao, 1,4) || '-' || SUBSTRING(dataLocacao, 5,2) || '-' || SUBSTRING(dataLocacao, 7,2)) as dataLocacao,
	idCliente, 
	idVendedor, 
	idCarro, 
	qtdDiaria, 
	vlrDiaria, 
	DATE(SUBSTRING(dataEntrega , 1,4) || '-' || SUBSTRING(dataEntrega, 5,2) || '-' || SUBSTRING(dataEntrega, 7,2)) as dataEntrega
FROM tb_locacao;


SELECT * FROM [fato_locacao];


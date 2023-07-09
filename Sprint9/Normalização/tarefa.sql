CREATE TABLE tb_combustivel (
	idCombustivel INT NOT NULL,
	tipoCombustivel VARCHAR, 
	PRIMARY KEY (idCombustivel)
);

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;

-----------------------------------------------

CREATE TABLE tb_cliente (
	idCliente INT NOT NULL,
	nomeCliente VARCHAR, 
	cidadeCliente VARCHAR, 
	estadoCliente VARCHAR,
	paisCliente VARCHAR,
	PRIMARY KEY (idCliente)
);

INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

----------------------------------------------

CREATE TABLE tb_vendedor (
	idVendedor INT NOT NULL,
	nomeVendedor VARCHAR, 
	sexoVendedor INT, 
	estadoVendedor VARCHAR,
	PRIMARY KEY (idVendedor)
);

INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao

---------------------------------------------

CREATE TABLE tb_carro (
	idCarro INT NOT NULL,
	classiCarro VARCHAR, 
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idcombustivel INT NOT NULL,
	PRIMARY KEY (idCarro),
	FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

INSERT INTO tb_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao;

---------------------------------------------

CREATE TABLE tb_kmRodados (
	idLocacao INT NOT NULL,
	kmCarro INT,
	FOREIGN KEY (idLocacao) REFERENCES tb_locacao(idLocacao)
);

INSERT INTO tb_kmRodados (idLocacao, kmCarro)
SELECT DISTINCT idLocacao, kmCarro
FROM tb_locacao;

--------------------------------------------

ALTER TABLE tb_locacao 
RENAME TO tb_locacao_antiga;

-------------------------------------------

CREATE TABLE tb_locacao (
	idLocacao INT PRIMARY KEY,
	idCliente INT,
	idVendedor INT,
	idCarro INT,
	dataLocacao VARCHAR,
	qtdDiaria INT,
	vlrDiaria INT,
	dataEntrega VARCHAR,
	horaEntrega VARCHAR,
	FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor),
	FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro)
);

INSERT INTO tb_locacao (idLocacao, idCliente, idVendedor, idCarro, dataLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idVendedor, idCarro, dataLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao_antiga;





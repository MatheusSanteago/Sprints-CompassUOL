# Tarefa 2 - Spark

##### Bibliotecas utilizadas

> **from operator import add** > **import re**

> **arquivo = sc.textFile("README.md")**

- Abrindo arquivo

> **palavras = arquivo.flatMap(lambda line: re.split('\W+', line.lower().strip()))**

- Separando as palavras utilizando regex _\W+_
  (Essa regex da match com os espaços em branco, então pega apenas as palavras)
> **filtradas = palavras.filter(lambda x: x not in (' !#$%&"()\*+,-./:;<=>?@[\]^\_`{|}~'))**
- Aqui é aplicado um filtro que desconsidera os caracteres especiais no README.
> **words = filtradas.map(lambda w: (w,1))**
- Aqui as palavras filtradas são formatas em (key,1)
> **words = words.reduceByKey(add)**
- Na redução são agrupadas e com a função add, a formatação realizada é somada conforme as palavras sejam iguais.
> **words.collect()**
-  Aqui são exibidas as palavras e suas respectivas contagens 
> **ordenadas = words.map(lambda x:(x[1],x[0])).sortByKey(False)**
-  Aqui os elementos são ordenados de acordo com o número de repetições, passando o False no sortByKey(), conseguimos uma ordenação decrescente

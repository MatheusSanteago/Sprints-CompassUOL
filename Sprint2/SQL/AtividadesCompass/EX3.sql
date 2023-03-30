SELECT count(*) as quantidade, nome, estado, cidade FROM livro as l
LEFT JOIN editora as e ON e.codeditora =  l.editora 
LEFT JOIN endereco as ende ON e.endereco = ende.codendereco  
GROUP BY editora
ORDER BY quantidade DESC;


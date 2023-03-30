SELECT DISTINCT a.nome FROM autor as a 
LEFT JOIN livro l ON l.autor = a.codautor
LEFT JOIN editora e ON e.codeditora = l.editora 
LEFT JOIN endereco ec ON ec.codendereco = e.endereco
WHERE estado NOT LIKE '%PARANÁ%'
ORDER BY a.nome;
 

 
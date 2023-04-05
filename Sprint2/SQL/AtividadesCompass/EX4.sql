SELECT nome,codautor,nascimento, count(l.titulo) as quantidade FROM livro as l
FULL JOIN autor as a ON a.codautor = l.autor
GROUP BY nome
ORDER BY nome;
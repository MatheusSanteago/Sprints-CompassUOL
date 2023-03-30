SELECT nome FROM autor as a
FULL JOIN livro as l ON l.autor = a.codautor
WHERE l.titulo IS NULL
ORDER BY nome;
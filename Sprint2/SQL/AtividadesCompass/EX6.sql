SELECT codautor,nome,count(*) as quantidade_publicacoes FROM livro as l
LEFT JOIN autor as a ON a.codautor = l.autor
GROUP BY autor
ORDER BY quantidade_publicacoes DESC
LIMIT 1;
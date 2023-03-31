SELECT cdpro,nmcanalvendas,nmpro, sum(qtd) as quantidade_vendas FROM tbvendas t 
WHERE status = 'Concluído' and nmcanalvendas = 'Ecommerce'
GROUP BY cdpro
UNION
SELECT cdpro,nmcanalvendas,nmpro, sum(qtd) as quantidade_vendas FROM tbvendas t 
WHERE status = 'Concluído' and nmcanalvendas = 'Matriz'
GROUP BY cdpro
ORDER BY quantidade_vendas;
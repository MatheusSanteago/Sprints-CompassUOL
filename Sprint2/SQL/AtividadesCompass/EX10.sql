SELECT 
	nmvdd as vendedor, 
	sum(t.qtd * vrunt) as valor_total_vendas, 
	ROUND((sum(t.qtd * vrunt) * vend.perccomissao) / 100, 2) as comissao 
FROM tbvendas t
LEFT JOIN tbvendedor as vend on vend.cdvdd = t.cdvdd
WHERE status = 'Concluído'
GROUP BY t.cdvdd
ORDER BY comissao DESC; 
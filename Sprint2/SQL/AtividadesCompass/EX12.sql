SELECT cddep, nmdep, dtnasc, sum(t.qtd * t.vrunt) as valor_total_vendas from tbdependente dep 
LEFT JOIN tbvendedor ven on ven.cdvdd = dep.cdvdd 
LEFT JOIN tbvendas t ON t.cdvdd = ven.cdvdd
WHERE t.status = 'Concluído'
GROUP BY nmdep
ORDER BY valor_total_vendas ASC 
LIMIT 1;

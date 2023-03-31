SELECT cdcli, nmcli, SUM(qtd * vrunt) as gasto from tbvendas t
WHERE status = 'Concluído'
GROUP BY cdcli
ORDER BY gasto DESC 
LIMIT 1;
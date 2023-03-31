SELECT cdpro,nmpro FROM tbvendas t
WHERE (dtven BETWEEN '2014-02-03' AND '2018-02-02') AND status = 'Concluído'
GROUP BY cdpro 
HAVING COUNT(cdpro)
ORDER BY COUNT(cdpro) DESC
LIMIT 1; 
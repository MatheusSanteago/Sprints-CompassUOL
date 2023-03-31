SELECT t.cdvdd,nmvdd from tbvendas t
LEFT JOIN tbvendedor as vend on vend.cdvdd = t.cdvdd
GROUP BY t.cdvdd
HAVING count(vend.nmvdd)
ORDER BY count(vend.nmvdd) DESC
LIMIT 1;

select estado , nmpro, ROUND(ROUND(sum(qtd),4) / COUNT(*),4) as quantidade_media from tbvendas t2
where status = 'Concluído' and nmpro LIKE '%A%'
GROUP by estado
UNION 
select estado , nmpro,  ROUND(ROUND(sum(qtd),4) / COUNT(*),4) as quantidade_media from tbvendas t2
where status = 'Concluído' and nmpro LIKE '%C%'
GROUP by estado
UNION 
select estado , nmpro,  ROUND(ROUND(sum(qtd),4) / COUNT(*),4) as quantidade_media from tbvendas t2
where status = 'Concluído' and nmpro LIKE '%CH%'
GROUP by estado
UNION 
select estado , nmpro,  ROUND(ROUND(sum(qtd),4) / COUNT(*),4) as quantidade_media from tbvendas t2
where status = 'Concluído' and nmpro LIKE '%TN%'
GROUP by estado
UNION 
select estado , nmpro,  ROUND(ROUND(sum(qtd),4) / COUNT(*),4) as quantidade_media from tbvendas t2
where status = 'Concluído' and nmpro LIKE '%SL%'
GROUP by estado
UNION 
select estado , nmpro, ROUND(ROUND(sum(qtd),4) / COUNT(*),4) as quantidade_media from tbvendas t2
where status = 'Concluído' and nmpro LIKE '%E%'
GROUP by estado
ORDER BY estado ;
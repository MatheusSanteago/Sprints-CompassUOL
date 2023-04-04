select estado, ROUND(AVG(qtd * vrunt),2) as gastomedio from tbvendas t2
where status = 'Concluído'
group by estado
order by gastomedio desc;
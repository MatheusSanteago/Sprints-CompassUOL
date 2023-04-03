select estado , nmpro, ROUND(AVG(qtd),4) as quantidade_media from tbvendas
where status = 'Concluído'
GROUP by estado, nmpro;
## EXERCÍCIOS 
###### SEÇÃO 1

### Exercício 1 

Identifique quais as marcas de veículo mais visitada na tabela sales.funnel

	select brand,count(visit_page_date) as vendas
	from sales.funnel as f
	left join sales.products as p on (f.product_id = p.product_id)
	group by brand
	order by vendas desc;
	
### Exercício 2

Identifique quais as lojas de veículo mais visitadas na tabela sales.funnel

	select store_name as store,count(visit_page_date) as visitas
	from sales.funnel as f
	left join sales.stores as s on (f.store_id  = s.store_id)
	group by store_name
	order by visitadas desc;

### Exercício 3 

Identifique quantos clientes moram em cada tamanho de cidade (o porte da cidade
consta na coluna "size" da tabela temp_tables.regions)

	select reg.size, count(*) as contagem
	from sales.customers as cus
	left join temp_tables.regions as reg
		on lower(cus.city) = lower(reg.city)
		and lower(cus.state) = lower(reg.state)
	group by reg.size
	order by contagem;

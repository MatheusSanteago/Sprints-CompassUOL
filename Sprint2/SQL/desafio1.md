## EXERCÍCIOS 
###### SEÇÃO 1

### Exercício 1 

Selecione os nomes de cidade distintas que existem no estado de
Minas Gerais em ordem alfabética (dados da tabela sales.customers)

    select distinct city 
    from sales.customers c 
    where state = 'MG'
    order by city asc;

### Exercício 2 
Selecione o visit_id das 10 compras mais recentes efetuadas
(dados da tabela sales.funnel)

    select visit_id
    from sales.funnel f 
    where paid_date is not null
    order by paid_date desc
    limit 10;

### Exercício 3 
Selecione todos os dados dos 10 clientes com maior score nascidos
pós 01/01/2000 (dados da tabela sales.customers)

    select *
    from sales.customers c 
    where birth_date > '2000-01-01'
    order by score desc
    limit 10;



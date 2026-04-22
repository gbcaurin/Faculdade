/* Exercicios de fixação */
/* Liste o nome dos funcionários e de seus dependentes. */
select funcionario.nome_funcionario, dependente.nome_dependente
from funcionario
inner join dependente
on funcionario.id_funcionario = dependente.id_funcionario;

/* Liste o nome dos funcionários e de seus dependentes, incluindo funcionários sem dependentes. */
select funcionario.nome_funcionario, dependente.nome_dependente
from funcionario
left join dependente
on funcionario.id_funcionario = dependente.id_funcionario;

/* Gere um relatório com cliente, produto e data da compra. */
select cliente.nome, produto.nome, compra.data_compra
from compra
inner join produto
on compra.id_produto = produto.id;
inner join cliente
on compra.id_cliente = cliente.id;

/* Liste as compras de um cliente específico. */
select cliente.nome, produto.nome, compra.data_compra
from compra
inner join produto
on compra.id_produto = produto.id;
inner join cliente
on compra.id_cliente = cliente.id;
where cliente.nome = "John Doe"

/* Liste todos os produtos, inclusive os que ainda não foram comprados. */
select produto.nome
from compra
left join produto
on compra.id_produto = produto.id;

/* Liste todos os clientes, inclusive os que ainda não fizeram compras. */
select cliente.nome
from compra
left join cliente
on compra.id_cliente = cliente.id;



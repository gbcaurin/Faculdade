/* Primeiro teste com join */
CREATE TABLE funcionario (
	id_funcionario INT PRIMARY KEY,
    nome_funcionario VARCHAR(50),
    setor VARCHAR(40)
);

CREATE TABLE dependente (
	id_dependente INT PRIMARY KEY,
    nome_dependente VARCHAR(50),
    id_funcionario INT,
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
);

/* Inserts criei com o copilot */

SELECT funcionario.nome_funcionario, dependente.nome_dependente FROM funcionario INNER JOIN dependente ON funcionario.id_funcionario = dependente.id_funcionario;

SELECT funcionario.nome_funcionario, dependente.nome_dependente FROM funcionario LEFT JOIN dependente ON funcionario.id_funcionario = dependente.id_funcionario;

SELECT funcionario.nome_funcionario, dependente.nome_dependente FROM funcionario RIGHT JOIN dependente ON funcionario.id_funcionario = dependente.id_funcionario;

SELECT funcionario.nome_funcionario, dependente.nome_dependente FROM funcionario INNER JOIN dependente ON funcionario.id_funcionario = dependente.id_dependente WHERE funcionario.setor = "T.I";



/* Segundo teste com join */
CREATE TABLE cliente (
	id INT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE produto (
	id INT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE compra (
	id INT PRIMARY KEY,
    id_cliente INT,
    id_produto INT,
    data_compra DATE,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);

/* Inserts criei com o copilot */

select cliente.nome, produto.nome, compra.data_compra
 from compra 
 inner join cliente 
 on compra.id_cliente = cliente.id 
 inner join produto 
 on compra.id_produto = produto.id;
 
select cliente.nome, produto.nome, compra.data_compra
 from compra 
 inner join cliente 
 on compra.id_cliente = cliente.id 
 inner join produto 
 on compra.id_produto = produto.id
 where cliente.nome = "Marcos";
 
 select cliente.nome, produto.nome, compra.data_compra
  from compra 
  inner join cliente 
  on compra.id_cliente = cliente.id 
  inner join produto 
  on compra.id_produto = produto.id
  order by compra.data_compra desc;
  
select produto.nome, cliente.nome, compra.data_compra
 from produto
 left join compra
 on produto.id = compra.id_produto
 left join cliente
 on compra.id = cliente.id;

select cliente.nome, produto.nome, compra.data_compra
 from cliente
 left join compra
 on cliente.id = compra.id_cliente
 left join produto
 on compra.id_produto = produto.id;
 
 


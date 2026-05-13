CREATE DATABASE aula_func_agregacoes;

USE aula_func_agregacoes;

CREATE TABLE venda (
	id INT PRIMARY KEY AUTO_INCREMENT,
    cliente VARCHAR(50),
    produto VARCHAR(50),
    categoria VARCHAR(50),
    quantidade INT,
    valor_u DECIMAL(10, 2),
    data DATE
);

INSERT INTO venda (cliente, produto, categoria, quantidade, valor_u, data) VALUES
('Ana Souza', 'Notebook', 'Informática', 1, 3500.00, '2025-05-01'),
('Bruno Lima', 'Mouse', 'Informática', 2, 80.00, '2025-05-02'),
('Carla Mendes', 'Teclado', 'Informática', 1, 150.00, '2025-05-03'),
('Ana Souza', 'Cadeira Gamer', 'Móveis', 1, 1200.00, '2025-05-04'),
('Eduarda Silva', 'Mesa de Escritório', 'Móveis', 1, 900.00, '2025-05-05'),
('Bruno Lima', 'Monitor', 'Informática', 2, 950.00, '2025-05-06'),
('Gabriela Costa', 'Caneta', 'Papelaria', 10, 3.50, '2025-05-07'),
('Henrique Dias', 'Caderno', 'Papelaria', 5, 25.00, '2025-05-08'),
('Carla Mendes', 'Impressora', 'Informática', 1, 750.00, '2025-05-09'),
('João Pedro', 'Estante', 'Móveis', 1, 650.00, '2025-05-10');

SELECT * FROM venda;

SELECT COUNT(*) AS total_vendas FROM venda;

SELECT COUNT(cliente) AS registros_cliente FROM venda;

SELECT COUNT(DISTINCT cliente) AS total_cliente_diferentes FROM venda;

SELECT COUNT(*) AS total_vendas_ti FROM venda WHERE categoria = "Informática";

SELECT AVG(valor_u) AS media_valor_u FROM venda;

SELECT AVG(quantidade) AS media_quantidade FROM venda;

SELECT AVG(valor_u) AS media_ti FROM venda WHERE categoria = "Informática";

SELECT SUM(quantidade) AS total_itens_vendidos FROM venda;

SELECT SUM(valor_u) AS soma_valores_u FROM venda;

SELECT SUM(quantidade * valor_u) AS faturamento_total FROM venda;

SELECT MIN(valor_u) AS menor_valor FROM venda;

SELECT MIN(quantidade) AS menor_quantidade FROM venda;

SELECT MIN(data) AS primeira_venda FROM venda;

SELECT MAX(valor_u) AS maior_valor FROM venda;

SELECT MAX(quantidade) AS maior_qtd FROM venda;

SELECT MAX(data) AS ultima_venda FROM venda;

SELECT categoria, COUNT(*) AS total_vendas FROM venda GROUP BY categoria;

SELECT categoria, SUM(quantidade) AS total_items FROM venda GROUP BY categoria;

SELECT categoria, SUM(quantidade * valor_u) AS faturamento_categ FROM venda GROUP BY categoria;

SELECT categoria, AVG(valor_u) AS media_valor FROM venda GROUP BY categoria;

SELECT cliente, COUNT(*) AS total_compras FROM venda GROUP BY cliente;
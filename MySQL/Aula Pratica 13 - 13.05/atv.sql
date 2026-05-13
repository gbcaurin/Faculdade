/* Mostre o total de vendas */
SELECT COUNT(*) AS total_vendas FROM venda;
/* Mostre quantos clientes diferentes fizeram compras */
SELECT COUNT(DISTINCT cliente) AS clientes_difeb
SELECT AVG(valor_u) AS media_valores FROM venda;
/* Mostre a soma total das quantidades vendidas */
SELECT SUM(quantidade) AS qtd_vendida FROM venda;
/* Mostre o maior valor unitário */
SELECT MAX(valor_u) AS maior_valor_u FROM venda;
/* Mostre o menor valor unitário */
SELECT MIN(valor_u) AS menor_valor_u FROM venda;
/* Mostre o faturamento total */
SELECT SUM(quantidade * valor_u) AS faturamento FROM venda;
/* Mostre a quantidade de vendas por categoria */
SELECT categoria, COUNT(*) FROM venda GROUP BY categoria;
/* Mostre o faturamento por categoria */
SELECT categoria, SUM(quantidade * valor_u) AS faturamento_por_categ FROM venda GROUP BY categoria;
/* Mostre a quantidade de compras por cliente */
SELECT cliente, COUNT(*) AS compras_realizadas FROM venda GROUP BY cliente;
/* Mostre a média de valores unitários por produto na categoria "Informática" */
SELECT produto, AVG(valor_u) AS media_por_produto FROM venda WHERE categoria = "Informática" GROUP BY produto;
/* Mostre a data da venda mais recente */
SELECT MAX(data) AS venda_mais_recente FROM venda;

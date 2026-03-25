CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nome VARCHAR(50),
  profissao VARCHAR(50),
  nacionalidade VARCHAR(30),
  altura DECIMAL(4,2)
);

INSERT INTO cliente VALUES 
(1, 'Ana', 'Professora', 'Brasileira', 1.65),
(2, 'Bruno', 'Desenvolvedor', 'Brasileiro', 1.80),
(3, 'Carlos', 'Analista', 'Alemao', 1.75),
(4, 'Diana', 'Engenheiro', 'Espanhol', 1.70);

SELECT * FROM cliente;

UPDATE cliente SET nacionalidade = 'Brasil' WHERE id = 1;
UPDATE cliente SET profissao = 'Engenheira', nacionalidade = 'Espanha' WHERE id = 4;
UPDATE cliente SET profissao = 'Dentista', nacionalidade = 'Irlanda' WHERE altura = 1.65;
TRUNCATE TABLE cliente; /* Remove todos os registros da tabela (basicamente um DELETE FROM cliente) */

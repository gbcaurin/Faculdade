CREATE TABLE funcionario (
  id INT PRIMARY KEY,
  nome VARCHAR(50),
  cargo VARCHAR(50),
  cidade VARCHAR(50),
  salario DECIMAL(10,2)
);

INSERT INTO funcionario VALUES 
(1, 'Ana', 'Desenvolvedora', 'São Paulo', 5000.00),
(2, 'Bruno', 'Analista', 'Rio de Janeiro', 6000.00),
(3, 'Carlos', 'Gerente', 'Belo Horizonte', 7000.00),
(4, 'Diana', 'Engenheira', 'Curitiba', 8000.00);

SELECT * FROM funcionario;

UPDATE funcionario SET cidade = 'São Paulo' WHERE id = 4;
UPDATE funcionario SET cargo = 'Gerente de Projetos', salario = 7500.00 WHERE id = 3;
DELETE FROM funcionario WHERE id = 2;
TRUNCATE TABLE funcionario;
#Aprendendo ALTER para alterar a tabela.

CREATE TABLE  carro(
	chassi INT PRIMARY KEY,
    fabricante VARCHAR (40),
    modelo VARCHAR(40),
    placa VARCHAR(10)
    );
    
SELECT * FROM carro;
SELECT * FROM carros;

ALTER TABLE carro ADD cor VARCHAR(20);
ALTER TABLE carro  MODIFY cor VARCHAR(15);
ALTER TABLE carro CHANGE cor cor_c VARCHAR(15);
RENAME TABLE carro TO carros;
ALTER TABLE carros DROP COLUMN fabricante;

---------------------------------------------------------

#Teste Solo

CREATE TABLE aluno(
	ra INT PRIMARY KEY,
    nome VARCHAR(50),
    curso VARCHAR(50)
);
SELECT * FROM aluno;
SELECT * FROM alunos;

ALTER TABLE aluno ADD email VARCHAR(50);
ALTER TABLE aluno MODIFY email VARCHAR(100);
ALTER TABLE aluno CHANGE curso curso_aluno VARCHAR(50);
RENAME TABLE aluno TO alunos;
ALTER TABLE alunos DROP COLUMN email;
DROP TABLE alunos;

---------------------------------------------------------

#Resumo comando MySQL
ADD adiciona uma nova coluna.
MODIFY altera tipo ou tamanho de uma coluna existente.
CHANGE renomeia uma coluna.
RENAME TABLE renomeia a tabela.
DROP COLUMN remove uma coluna.
DROP TABLE remove a tabela inteira.




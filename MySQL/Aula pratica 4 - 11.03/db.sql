#Comandos Basicos do SQL

CREATE TABLE livro (
id INT PRIMARY KEY,
titulo VARCHAR(150),
autor VARCHAR(100),
ano_publicacao INT
);

INSERT INTO livro VALUES (1, 'Dom Casmurro', 'Machado de Assis', 1899);
INSERT INTO livro VALUES (2, 'O Hobbit', 'J.R.R. Tolkien', 1937);

SELECT * FROM livro;
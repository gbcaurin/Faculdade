CREATE TABLE autor (
	id INT PRIMARY KEY,
    nome VARCHAR(50),
    nacionalidade VARCHAR(50)
);

CREATE TABLE livro (
	id INT PRIMARY KEY,
    titulo VARCHAR(50),
    ano_publicacao INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autor(id)
);

CREATE TABLE emprestimo (
	id INT PRIMARY KEY,
    nome_aluno VARCHAR(50),
    data_emprestimo DATE,
    data_devolucao DATE,
    status VARCHAR(25),
    id_livro INT,
    FOREIGN KEY (id_livro) REFERENCES livro(id)
);


INSERT INTO autor VALUES 
(1, "J.R.R Tolkien", "Britânico"),
(2, "J.K Rowling", "Britânica"),
(3, "Machado de Assis","Brasileiro");
INSERT INTO livro VALUES 
(1, "A Sociedade do Anel", 1954, 1),
(2, "As Duas Torres", 1954, 1),
(3, "O Retorno do Rei", 1955, 1),
(4, "Harry Potter e a Pedra Filosofal", 1997, 2),
(5, "Dom Casmurro", 1899, 3);
INSERT INTO emprestimo VALUES 
(1, "Gabriel Caurin", "2026-02-15", NULL, "Emprestado", 3),
(2, "Gabriel Caurin", "2026-01-29", "2026-03-13", "Devolvido", 1),
(3, "Gabriel Caurin", "2025-08-16", "2025-10-01", "Devolvido", 2),
(4, "Enrico Locateli", "2026-05-06", NULL, "Emprestado", 4),
(5, "Enrico Locateli", "2026-02-22", "2025-05-06", "Devolvido", 5);

/* Selecionar todos os autores */
SELECT * FROM autor;

/* Selecionar todos os livros */
SELECT * FROM livro;

/* Selecionar todos os livros ordenados pelo título */
SELECT * FROM livro ORDER BY titulo;

/* Selecionar todos os autores cujo nome contém a letra "a" */
SELECT * FROM autor WHERE nome LIKE "%a%";

/* Selecionar todos os livros publicados antes de 1955 */
SELECT * FROM livro WHERE ano_publicacao < 1955;

/* Selecionar o título do livro e o nome do autor */
SELECT livro.titulo, autor.nome FROM livro INNER JOIN autor ON livro.id_autor = autor.id;

/* Selecionar o nome do aluno, o título do livro, a data de empréstimo e o status */
SELECT emprestimo.nome_aluno, livro.titulo, emprestimo.data_emprestimo, emprestimo.status FROM emprestimo INNER JOIN livro ON emprestimo.id_livro = livro.id;

/* Selecionar todos os empréstimos ativos */
SELECT * FROM emprestimo WHERE status = "Emprestado";

/* Selecionar o nome do autor e o título do livro mesmo se o autor não estiver associado a nenhum livro */
SELECT autor.nome, livro.titulo FROM livro LEFT JOIN autor ON livro.id_autor = autor.id;

/* Selecionar todos os livros e seus empréstimos, mesmo que não tenham sido emprestados */
SELECT * FROM livro LEFT JOIN emprestimo ON emprestimo.id_livro = livro.id;



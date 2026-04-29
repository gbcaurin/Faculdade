CREATE TABLE curso (
	id INT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE aluno (
	id INT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(50),
    curso_id INT,
    FOREIGN KEY (curso_id) REFERENCES curso(id)
);

INSERT INTO curso VALUES (1, "Engenharia de Software"),(2, "Sistema da Informação"),(3, "Cybersegurança");
INSERT INTO aluno VALUES (1, "Gabriel Caurin", "gbcaurin@puc.edu.br", 1),(2, "Enrico Locateli", "erlocateli@puc.edu.br", 1),(3, "Matheus Teodoro", "mtteodoro@puc.edu.br", 3),(4, "Lívia Souza", "lvsouza@puc.edu.br", NULL);

/* Selecione todos alunos */
SELECT * FROM aluno;
/* Selecione apenas o nome dos alunos */
SELECT nome FROM aluno;
/* Selecione alunos com ID maior que 1 */
SELECT * FROM aluno WHERE id > 1;
/* Selecione alunos e o nome do curso a que pertencem */
SELECT aluno.nome, curso.nome FROM aluno INNER JOIN curso ON aluno.curso_id = curso.id;
/* Selecione alunos de um curso específico */
SELECT aluno.nome, curso.nome FROM aluno INNER JOIN curso ON aluno.curso_id = curso.id WHERE curso.nome = "Engenharia de Software";

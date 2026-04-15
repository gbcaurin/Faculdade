CREATE TABLE curso(
	id_curso INT PRIMARY KEY,
    nome_curso VARCHAR(50)
);

CREATE TABLE aluno (
	id_aluno INT PRIMARY KEY,
    nome_aluno VARCHAR(50),
    id_curso INT,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
    );
    
    INSERT INTO curso (id_curso, nome_curso) VALUES (1, "Engenharia de Software"), (2, "Design Digital") , (3, "CyberSgurança");
    INSERT INTO aluno VALUES (1, "Gabriel Caurin", 1) , (2, "Enrico Locateli", 1) , (3, "Lívia de Souza", 2) , (4, "Gabriel de Novaes", 3) , (5, "João sem Dente", 1);
    
    DESCRIBE curso;
    DESCRIBE aluno;
    
    SELECT * FROM curso;
    SELECT * FROM aluno;
    

    /* Eu estava testando inner join por parte */
    SELECT curso.nome_curso FROM aluno INNER JOIN curso ON aluno.id_curso = curso.id_curso WHERE aluno.id_aluno = 1;
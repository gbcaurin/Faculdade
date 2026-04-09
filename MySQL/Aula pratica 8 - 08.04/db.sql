	CREATE TABLE aluno (
		ra INT PRIMARY KEY,
		nome VARCHAR(20),
		datanasc DATE,
		rg VARCHAR(13)
	);

	SELECT * FROM aluno;

	INSERT INTO aluno VALUES (1257139, "Ana Maria", "1978-09-05", "17555789"),(12673375, "Jose Carlos Mendes", "1981-11-03", "15229131"),(12673571, "Janaina Silva", NULL, "15237735"),(12673572, "Carlos ALberto", "1978-09-05", "15247736"),(12556670, NULL, NULL, NULL); 

	SELECT * FROM aluno WHERE NOME = "Ana Maria";

	SELECT * FROM aluno WHERE ra = 12673375;

	SELECT * FROM aluno WHERE rg = "17555789";

	SELECT * FROM aluno WHERE datanasc = "1978-09-05";

	SELECT nome, rg FROM aluno WHERE datanasc IS NOT NULL;

	SELECT * FROM aluno WHERE datanasc IS NULL;

	SELECT datanasc FROM aluno;

	SELECT DISTINCT datanasc FROM aluno;

	SELECT nome, datanasc FROM aluno WHERE  datanasc > "1978-09-05";

	SELECT * FROM aluno WHERE ra BETWEEN 12556670 AND 12673500;
    

  /* Selecionar todos nomes com nome Jose */  
  SELECT * FROM aluno WHERE nome LIKE"Jose%";
  /* Selecionar todos nomes que começam com J */  
  SELECT * FROM aluno WHERE nome LIKE"J%";
  /* Selecionar todos nomes que contêm a letra "a" */  
  SELECT * FROM aluno WHERE nome LIKE"%a%";
  /* Selecionar todos nomes que têm "n" como segunda letra (OBS: "_" representa qual letra você quer entao "___" pegaria a quarta letra) */  
  SELECT * FROM aluno WHERE nome LIKE"_n%";
  /* Selecionar todos alunos exceto os com RA 12673375 e 12673571 */  
  SELECT ra, nome FROM aluno WHERE ra NOT IN (12673375, 12673571);
  /* Ordenar alunos pelo RA */  
  SELECT * FROM aluno ORDER BY ra;
  /* Ordenar alunos pela data de nascimento */  
  SELECT * FROM aluno ORDER BY datanasc;
  /* Selecionar alunos com nomes que começam com "J" e ordená-los em ordem descendente */  
  SELECT ra, nome, rg FROM aluno WHERE nome LIKE"J%" ORDER BY nome DESC;
    
    
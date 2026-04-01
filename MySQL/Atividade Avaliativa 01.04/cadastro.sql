CREATE TABLE cadastro (
	cpf_ca VARCHAR(11) PRIMARY KEY,
	nome_ca VARCHAR(20),
    rg_ca VARCHAR(9)
);

INSERT INTO cadastro VALUES ("10988375542","Clara","185436789") , ("12033335686","Felipe","239856955") , ("10733211556","Renato","143256789");
SELECT * FROM cadastro;

RENAME TABLE cadastro TO consumidor;
SELECT * FROM consumidor;

ALTER TABLE consumidor ADD COLUMN fone VARCHAR(11);

ALTER TABLE consumidor MODIFY nome_ca VARCHAR(25);

ALTER TABLE consumidor CHANGE fone telefone_ca VARCHAR(11);

ALTER TABLE consumidor DROP COLUMN rg_ca;

ALTER TABLE consumidor CHANGE cpf_ca id_cpf VARCHAR(11);

DROP TABLE consumidor;
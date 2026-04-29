CREATE TABLE startup (
	id INT PRIMARY KEY,
	nome_startup VARCHAR(50),
	setor VARCHAR(40),
	estagio VARCHAR(30)
);

CREATE TABLE investidor (
id INT PRIMARY KEY,
nome_investidor VARCHAR(50),
email VARCHAR(60)
);

CREATE TABLE investimento (
id INT PRIMARY KEY,
investidor_id INT,
startup_id INT,
valor DECIMAL(10,2),
status VARCHAR(20),
FOREIGN KEY (investidor_id) REFERENCES investidor(id),
FOREIGN KEY (startup_id) REFERENCES startup(id)
);

INSERT INTO startup VALUES
(1, 'GreenPulse', 'Sustentabilidade', 'Operação'),
(2, 'HealthVision', 'Healthtech', 'Expansão'),
(3, 'EduSpark', 'Edtech', 'Ideia'),
(4, 'FinChain', 'Fintech', 'Operação');

INSERT INTO investidor VALUES
(1, 'Ana Souza', 'ana@email.com'),
(2, 'Bruno Lima', 'bruno@email.com'),
(3, 'Carla Mendes', 'carla@email.com'),
(4, 'Diego Alves', 'diego@email.com');

INSERT INTO investimento VALUES
(1, 1, 1, 10000.00, 'Confirmado'),
(2, 2, 2, 15000.00, 'Confirmado'),
(3, 1, 2, 5000.00, 'Pendente'),
(4, 3, 1, 8000.00, 'Confirmado');

SELECT * FROM startup;
SELECT * FROM investidor;
SELECT * FROM investimento;

SELECT nome_investidor, email FROM investidor;

SELECT * FROM investimento WHERE valor > 7000;

SELECT * FROM investidor ORDER BY nome_investidor;

SELECT investidor.nome_investidor, investimento.valor, investimento.status FROM investimento INNER JOIN investidor ON investimento.investidor_id = investidor_id;

SELECT startup.nome_startup, investimento.valor, investimento.status FROM investimento INNER JOIN startup ON investimento.startup_id = startup.id;

SELECT investidor.nome_investidor, startup.nome_startup, investimento.valor, investimento.status FROM investimento INNER JOIN investidor ON investimento.investidor_id = investidor.ID INNER JOIN startup ON investimento.startup_id = startup.id;

SELECT investidor.nome_investidor, startup.nome_startup, investimento.valor FROM investimento INNER JOIN investidor ON investimento.investidor_id = investidor.ID INNER JOIN startup ON investimento.startup_id = startup.id WHERE investimento.status = "Confirmado";

SELECT startup.nome_startup, investimento.valor, investimento.status FROM startup LEFT JOIN investimento ON investimento.startup_id = startup.id;

SELECT investidor.nome_investidor, investimento.valor, investimento.status FROM investimento RIGHT JOIN investidor ON investimento.investidor_id = investidor.id;
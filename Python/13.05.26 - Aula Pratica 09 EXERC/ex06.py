alunos = [1.70, 1.85, 1.65, 1.90, 1.75, 1.80, 1.75, 1.85, 1.80, 1.95]
S = 0
med = 0

for i in range(len(alunos)):
  S += alunos[i]

med = S / len(alunos)

for i in range(len(alunos)):
  if alunos[i] < med:
    print(f"Aluno com altura abaixo da média: {alunos[i]}")
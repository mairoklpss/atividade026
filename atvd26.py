# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0

lista = []
contador = 0
alunoQuantidade = 0

for i in range(1, 6):
    aluno = float(input(f"digite a nota do aluno {i}: "))
    lista.append(aluno)
    contador += 1
    alunoQuantidade += aluno
    media = alunoQuantidade/contador


print("maior nota:", max(lista))
print("menor nota:", min(lista))
print(f"media das notas: {media}")

"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
caderno_notas=[
    ["Maria", 6.0 , 8.0],
    ["Sophia", 8.0 , 9.0],
    ["Vanessa", 8.0 , 10.0]
]

print("\nBoletim da turma:")
for linha in caderno_notas:
    nome= linha[0]
    nota1= linha[1]
    nota2= linha[2]
    media=(nota1+nota2) / 2

    if media>=6.0:
        situacao="aprovado"
    else:
        situacao="reprovado"
    print(f"aluno:{nome},| média:{media}|situação:{situacao}")
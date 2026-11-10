"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web={"ana","vanessa","malu","sophia"}
alunos_banco={"karol","sophia","vanessa","samela"}

intersecao=alunos_web & alunos_banco
diferenca_1=alunos_web - alunos_banco
diferenca_2=alunos_banco - alunos_web

print(f"alunos das duas turma são:{intersecao}")
print(f"alunos web:{diferenca_1}")
print(f"alunos banco:{diferenca_2}")
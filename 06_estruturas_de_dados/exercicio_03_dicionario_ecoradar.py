"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:

aluno_ds={
    "2026-DS-60":"desenvolvedor",
    "2026-DS-30":"designer",
    "2026-DS-500": "cyber"
}

busca=input("digite a matrícula do aluno:")

print(f"o cargo etse aluno é:{aluno_ds[busca]}")
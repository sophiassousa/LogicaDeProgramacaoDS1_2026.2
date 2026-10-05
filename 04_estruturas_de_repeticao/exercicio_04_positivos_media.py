"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quantidades_positivos=0
soma_positivos=0.0
print("digite 6 valore numericos")
for i in range(6):
    valor=float(input(f"digite o valor {i+1}:"))
    if valor>0:
     quantidades_positivos+=1
soma_positivos+=valor
if quantidades_positivos>0:
    media=soma_positivos/quantidades_positivos
else:
    media=0.0
print(f"nQuantidade de positivos:{quantidades_positivos}")
print(f"media dos valores positivos:{media:.1f}")
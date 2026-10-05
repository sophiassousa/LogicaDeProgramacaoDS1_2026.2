"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
x= int(input("digite o 1° numero:"))
y= int(input("digite o 2° numero:"))
inicio=min(x,y)
fim=max(x,y)
print(f"\nNumeros entre {inicio} e {fim} com resto 2 ou 3 na divisão por 5:") 
for i in range(inicio,fim+1):
    resto= i%5
    if resto==2 or resto==3:
        print(i)
















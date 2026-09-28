"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
A=float(input("digite o valor de A:"))
B=float(input("digite o valo de B:"))
C=float(input("digite o valor de C:"))

delta=(B**2)-(4*A*C)

if delta < 0 or A == 0:
    print("imposivel calcular")
else:
    x1=(-B+delta**0.5)/(2*A)   
    x2=(-B+delta**0.5)/(2*A)
print(f"{x1:.5f}")
print(f"{x2:.5f}")     

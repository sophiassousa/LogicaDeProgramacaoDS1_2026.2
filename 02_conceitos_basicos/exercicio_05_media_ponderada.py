"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1=float(input("digite a primeira nota"))
nota2=float(input("digite a segunda nota"))
nota3=float(input("digite a terceira nota"))
calc1=nota1*2
calc2=nota2*3
calc3=nota3*5
soma_calc=(calc1+calc2+calc3)
media= soma_calc/(2+3+5) 
print("a média final é de", media) 
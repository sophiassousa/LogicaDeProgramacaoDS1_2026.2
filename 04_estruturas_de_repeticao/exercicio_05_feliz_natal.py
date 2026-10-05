"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:

i= int(input("digite o nivel de empolgação"))
contador_i=-1
for n in range(i):
    contador_i+=1
a=1+ contador_i
a="a"*a
print(f"feliz nat{a}l")



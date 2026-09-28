"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
nome=str(input("digite o seu nome:"))
idade=int(input("digite a sua idade:"))
ingresso=100

if idade<12:
    ingresso_1=100-50
    print(f"ingresso infantil:{ingresso_1} ")
elif idade>=60:
    print("melhor idade, é grátis") 
else:
    print(f"o ingresso custa:{ingresso}")      

"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
calcular_desconto=lambda valor: valor*0.85

preco=100

resultado= calcular_desconto(preco)

print(f"preço original:R${preco:.2f}")
print(f"preço com desconto:R${resultado:.2f}")
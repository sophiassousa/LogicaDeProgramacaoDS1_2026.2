"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
lista_mercado= ("maçã","banana","acerola","abacaxi","acerola","maçã")
lista_unica=set(lista_mercado)
print(f"lista:{lista_unica}")

inventario={
    "maçã" : 30,
    "abacaxi":40,
    "acerola":50,
    "banana":20
}

fruta_cliente=input("digite a fruta que deseja consultar no estoque:")

resposta=inventario.get(fruta_cliente,"fruta não encontrada no estoque")

print(f"reultado:{resposta}")



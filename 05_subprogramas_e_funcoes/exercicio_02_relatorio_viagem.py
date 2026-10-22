"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km,consumo_kml,preco_combustivel):
    litros=distancia_km/consumo_kml
    custo=litros*preco_combustivel
    return custo

    def calcular_custo_alimentacao(qtd_pessoas,dias,diaria_alimentacao):
        custo=qtd_pessoas*dias*diaria_alimentaçao
        return custo
        
distancia=float(input("distancia da viagem em km:"))
consumo=float(input("consumo do carro em km/l:"))
preco=float(input("preço do combustivel por litro:")) 

pessoas=int(input("quantidade de pessoas:"))
dias=int(input("quantidade de dias:"))
diaria=float(input("gasto diario com alimentação por pessoa:"))


custo_transporte=custo_transporte(distancia,consumo,preco)
custo_alimentacao=custo_alimentacao(pessoas,dias,diaria)

custo_total= custo_transporte + custo_alimentacao

print(f"cuto do transporte:R${custo_transporte:.2f}")
print(f"custo da alimentação:R${cuto_alimentaao:.2f}")
print(f"custo total a viagem:R${custo_total:.2f}")
"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:           
def calcular_pontuacao_total(fase_1,fase_2,fase_3):
    resultado=fase_1+fase_2+fase_3
    return resultado


fase_1=int(input("digite a pontuação da fase 1:"))
fase_2=int(input("digite a pontuação da fase 2:"))
fase_3=int(input("digite a pontuação da fase 3:"))

resultado=calcular_pontuacao_total(fase_1,fase_2,fase_3)
print(resultado)


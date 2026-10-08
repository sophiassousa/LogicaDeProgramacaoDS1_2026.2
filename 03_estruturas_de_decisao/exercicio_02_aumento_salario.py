"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input("digite o salario:"))
if salario >=0.00 and salario<=400.00:
    salario_1=(salario*0.15)+salario
    print("novo salario:",salario_1)
    print("valor do reajuste:",salario_1-salario)
    print("porcentual aplicado:15%")
elif salario>=400.01 and salario<=800.00:
    salario_2=(salario*0.12)+ salario
    print("novo salario:",salario_2)
    print("valor do reajuste:",salario_2-salario)
    print("porcentual aplicado:12%")
elif salario>=800.01 and salario<=100.00:
    salario_3=(salario*0.10)+ salario
    print("novo salario:",salario)
    print("valor do reajuste:",salario_3-salario)
    print("porcentual aplicado:10%")
elif salario>=1200.01 and salario<=2000.00:
    salario_4=(salario*0.07)+ salario
    print("novo salario:",salario)  
    print("valor do reajuste:",salario_4-salario)
    print("porcentual aplicado:7%")
elif salario>2000.00:
    salario_5=(salario*0.04)+salario
    print("novo salario:",salario) 
    print("valor do reajuste:",salario_5-salario)
    print("porcentual aplicado:4%")    



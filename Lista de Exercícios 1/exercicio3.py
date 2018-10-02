"""
     Victor Luiz da Silva Mariano Pereira

     Lista de Exercícios 1
     Exercício 3

     Descrição:
        Um fabricante produz copos e garrafas. Para isso, ele pode utilizar
        dois processos P1 e P2. A produção de copos leva 30 minutos usando o
        processo P1 e 20 minutos usando o processo P2. A produção de garrafas
        leva 35 minutos com o processo P1 e 40 com o processo P2. Devido à
        mão-de-obra disponível, só se pode utilizar, por semana, 40 horas do
        processo P1 e 30 horas do processo P2. Modele o problema de se
        organizar a produção de forma a ter um estoque máximo conjunto de copos
        e garrafas ao fim de uma semana.
"""

import pulp

model = pulp.LpProblem('exercicio3', pulp.LpMaximize)

# Variáveis
# quantidade de processos P1 para copos
c1 = pulp.LpVariable("c1", cat='Integer', lowBound=0)
# quantidade de processos P2 para copos
c2 = pulp.LpVariable("c2", cat='Integer', lowBound=0)
# quantidade de processos P1 para garrafas
g1 = pulp.LpVariable("g1", cat='Integer', lowBound=0)
# quantidade de processos P2 para garrafas
g2 = pulp.LpVariable("g2", cat='Integer', lowBound=0)

# Função objetivo
model += c1 + c2 + g1 + g2

# sujeito a
model += c1 * 30 + g1 * 35 <= 40 * 60, 'mao de obra disponivel processo P1'
model += c2 * 20 + g2 * 40 <= 30 * 60, 'mao de obra disponivel processo P2'
# model += c1 <= 0, 'valor nao negativo'
# model += c2 <= 0, 'valor nao negativo'
# model += g1 <= 0, 'valor nao negativo'
# model += g2 <= 0, 'valor nao negativo'

# Resolvendo
model.solve(pulp.solvers.GLPK())

for x in model.variables():
    print("{} = {}".format(x, x.value()))

# resultado da função objetivo
# print('O valor da solução é {}.'.format(model.objective.value()))

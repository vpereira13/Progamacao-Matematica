"""
     Victor Luiz da Silva Mariano Pereira

     Lista de Exercícios 1
     Exercício 2

     Descrição:
        Uma empresa de rádio de São Carlos constatou que o programa Parada
        Internacional , com 20 minutos de música e 1 minuto de propaganda chama
        a atenção de 30.000 ouvintes, enquanto o programa Top Tunes , com 10
        minutos de música e 1 minuto de propaganda chama a atenção de 10.000
        ouvintes. No decorrer de uma semana, o patrocinador insiste no uso de
        no mínimo 5 minutos para sua propaganda e que não há verba para mais de
        80 minutos de música. Quantas vezes por semana cada programa deve ser
        levado ao ar visando ter o número máximo de ouvintes?
"""

import pulp

model = pulp.LpProblem('exercicio2', pulp.LpMaximize)

# Variáveis
# quantidade de vezes que o programa PI será reproduzido na semana
xp = pulp.LpVariable("xp", cat='Integer', lowBound=0)
# quantidade de vezes que o programa TT será reproduzido na semana
xt = pulp.LpVariable("xt", cat='Integer', lowBound=0)

# Função objetivo
model += 30000 * xp + 10000 * xt

# sujeito a
model += xp * 20 + xt * 10 <= 80, 'maximo de verba'
model += xp + xt >= 5, 'minimo de propaganda'
# model += xt >=0, 'valor nao negativo'
# model += xp >=0, 'valor nao negativo'

# Resolvendo
model.solve(pulp.solvers.GLPK())

for x in model.variables():
    print("{} = {}".format(x, x.value()))

# resultado da função objetivo
# print('O valor da solução é {}.'.format(model.objective.value()))

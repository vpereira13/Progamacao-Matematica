"""
     Victor Luiz da Silva Mariano Pereira

     Lista de Exercícios 1
     Exercício 1

     Descrição:
        Júlio começou a estudar no ICMC e já percebeu que só estudar e não se
        divertir faz dele um bobalhão. Assim, ele quer partilhar seu tempo de
        aproximadamente 10 horas por dia entre estudo e diversão. Ele estima
        que divertir é duas vezes mais interessante que estudar e, além disso,
        ele quer estudar pelo menos o mesmo tempo que dedica para diversão.
        Entretanto, Júlio percebeu que, para realizar todas as suas atividades,
        não poderá se divertir mais que 4 horas por dia. Como ele deve
        distribuir o tempo para maximizar seu prazer em termos de estudo e
        diversão?
"""

import pulp

model = pulp.LpProblem('exercicio1', pulp.LpMaximize)

td = pulp.LpVariable("td", lowBound=0)  # tempo de estudo
te = pulp.LpVariable("te", lowBound=0)  # tempo de diversão

model += 2*td + te  # função objetivo

# sujeito a
model += td + te <= 10, 'tempo maximo de estudo'
model += te >= td, 'tempo de estudo maior que de diversao'
model += td <= 4, 'no maximo 4h de diversao'
# model += td >= 0, 'valor nao negativo'
# model += te >= 0, 'valor nao negativo'

# resolvendo
model.solve(pulp.solvers.GLPK())

for x in model.variables():
    print("{} = {}".format(x, x.value()))

# resultado da função objetivo
# print('O valor da solução é {}.'.format(model.objective.value()))

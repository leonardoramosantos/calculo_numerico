"""
Script criado para a matéria de Cálculo Numérico para encontrar a raiz de uma
função usando o método de Bissecção.

Substituir os valores:

y = função
erro_maximo = Erro Máximo aceitável
p_x_inicial = Ponto X inicial para procurar a Raiz
p_x_final = Ponto X final para procurar a Raiz

"""

import termplotlib as tpl
import numpy

from BisectionRootFinder import BisectionRootFinder
from imports import START_X_AXYS
from imports import END_X_AXYS
from imports import SAMPLES_X_AXYS

x = numpy.linspace(START_X_AXYS, END_X_AXYS, SAMPLES_X_AXYS)
# y = (numpy.power(x, 2) * -9.81)/2 + (30 * x) + 5
# erro_maximo = 0.04
# p_x_inicial = 6
# p_x_final = 7

# y = (9 * numpy.exp(-x) * numpy.sin(2 * numpy.pi * x)) - 4
# erro_maximo = 0.00001
# # p_x_inicial = 0
# # p_x_final = 0.2
# p_x_inicial = 0.225
# p_x_final = 1

# y = (numpy.power(x, 2) * -9.81)/2 + (30 * x) + 5
# erro_maximo = 0.04
# p_x_inicial = 6
# p_x_final = 7

y = (2 * x) - (500 / numpy.power((x - 3), 2))
erro_maximo = 0.0015
p_x_inicial = 8
p_x_final = 9

fig = tpl.figure()
fig.plot(x, y, label="f(x)", width=100, height=20)
fig.show()

rf = BisectionRootFinder(y, p_x_inicial, p_x_final, erro_maximo)
rf.start_plotting()

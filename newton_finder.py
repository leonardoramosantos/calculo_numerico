import termplotlib as tpl
import numpy

from NewtonRootFinder import NewtonRootFinder
from imports import START_X_AXYS
from imports import END_X_AXYS
from imports import SAMPLES_X_AXYS

x = numpy.linspace(START_X_AXYS, END_X_AXYS, SAMPLES_X_AXYS)

# Exerc 1 
# y = 4 * numpy.cos(x) - numpy.exp(2 * x)
# y_d = -4 * numpy.sin(x) - 2 * numpy.exp(2 * x)

# Exerc 2
# y = numpy.power(2, x) - 3 * x
# y_d = numpy.power(2, x) * numpy.log2(2) - 3

# Exerc 3
# y = numpy.power(x, 5) - (3 * numpy.power(x, 3)) + (2 * numpy.power(x, 2)) - (3 * x) + 1
# y_d = (5 * numpy.power(x, 4)) - (9 * numpy.power(x, 2)) + (4 * x) - 3

# Exerc 4
# y = 1 - (x * numpy.log(x))
# y_d = -numpy.log(x) - 1

# Prova 2
y = 15 + (50 * x) - (9.81 * numpy.power(x, 2) / 2)
y_d = 50 - (9.81 * x)

erro_maximo = 0.001
p_x_inicial = 10

fig = tpl.figure()
fig.plot(x, y, label="f(x)", width=100, height=20)
fig.show()

rf = NewtonRootFinder(y, p_x_inicial, max_error=erro_maximo, derivative=y_d)
rf.start_plotting()

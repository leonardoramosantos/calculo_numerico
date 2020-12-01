import termplotlib as tpl
import numpy

# START_X_AXYS = 1
# END_X_AXYS = 5
# SAMPLES_X_AXYS = 17

START_X_AXYS = 1.5
END_X_AXYS = 4.5
SAMPLES_X_AXYS = 7

x = numpy.linspace(START_X_AXYS, END_X_AXYS, SAMPLES_X_AXYS)
y = 0.6666666 * numpy.power(x, 4) - \
    7.3333333 * numpy.power(x, 3) + \
    27.1666666 * numpy.power(x, 2) - \
    57.8809523 * x + \
    127.0952381

fig = tpl.figure()
fig.plot(x, y, label="f(x)", width=100, height=20)
fig.show()

area = 0.0
for i in range(0, SAMPLES_X_AXYS):
    if (i == 0) or (i == SAMPLES_X_AXYS - 1):
        area += y[i]
        # print("Somando {} # {}".format(i, y[i]))
    else:
        area += (y[i] * 2)
        # print("Somando {} # {}".format(i, y[i]))

div = (END_X_AXYS - START_X_AXYS) / (SAMPLES_X_AXYS - 1) / 2

# print("Area Antes da divisao {}".format(area))

area = div * area

print("Area final {} # Subintervalos {}".format(area, SAMPLES_X_AXYS - 1 ))
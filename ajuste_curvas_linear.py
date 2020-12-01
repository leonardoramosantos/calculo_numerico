from imports import ROUND_FLOATS

x = [0.5, 2.8, 4.2, 6.7, 8.3]
y = [4.4, 1.8, 1.0, 0.4, 0.2]

x_2 = []
x_y = []

print("TABELA")
print("########################################################################")


for idx in range(0, len(x)):
    x_2.append(x[idx] * x[idx])
    x_y.append(x[idx] * y[idx])

    print("{} # {} # {} # {} # {}".format(
        str(round(idx, ROUND_FLOATS)).rjust(12), 
        str(round(x[idx], ROUND_FLOATS)).rjust(12), 
        str(round(y[idx], ROUND_FLOATS)).rjust(12), 
        str(round(x_2[idx], ROUND_FLOATS)).rjust(12), 
        str(round(x_y[idx], ROUND_FLOATS)).rjust(12)))

print("{} # {} # {} # {} # {}".format(
    " SOMA       ", 
    str(round(sum(x), ROUND_FLOATS)).rjust(12), 
    str(round(sum(y), ROUND_FLOATS)).rjust(12), 
    str(round(sum(x_2), ROUND_FLOATS)).rjust(12), 
    str(round(sum(x_y), ROUND_FLOATS)).rjust(12)))

print("########################################################################")


sistema_final = [[sum(x_2), sum(x)], [sum(x), len(x)]]
result_sistema = [sum(x_y), sum(y)]

mult = sistema_final
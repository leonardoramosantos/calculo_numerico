# # Exemplo 1 
# matrix = [[10, 2, 1],
#           [1, 16, 3],
#           [1, 3, 10]]
# results = [6, 8, 7]
# aprox = [0.6, 0.5, 0.7]
# max_error = 0.05

# # Exemplo 2
matrix = [[5, 2, 2],
          [1, 3, 1],
          [0, 6, 8]]
results = [-1, -2, -6]
aprox = [0, 0, 0]
max_error = 0.2

# GB - 1
# matrix = [[10, 2, 1],
#           [1, -15, 1],
#           [2, 3, 10]]
# results = [7, 32, 6]
# aprox = [0, 0, 0]
# max_error = 0.001

# GB - 2a
# matrix = [[1, 1, 1],
#           [0, 1, 2],
#           [0, 0, -3]]
# results = [3, 2, -2]
# aprox = [0, 0, 0]
# max_error = 0.001

# GB - 2b
# matrix = [[1, 1, 1],
#           [0, 1, 2],
#           [0, 0, 0]]
# results = [3, 2, 0]
# aprox = [0, 0, 0]
# max_error = 0.001

# GB - 2c
# matrix = [[1, 1, 1],
#           [0, 1, 1],
#           [0, 0, 0]]
# results = [-10, -40, -40]
# aprox = [0, 0, 0]
# max_error = 0.001

# GB - 3
# matrix = [[1, 10, 1, 2, 2],
#           [9, 1, 0, 1, 1],
#           [2, 2, 5, 1, 2],
#           [1, 1, 1, 2, 13],
#           [1, 1, 1, 9, 2]]
# results = [170, 180, 150, 180, 350]
# aprox = [0, 0, 0, 0, 0]
# max_error = 0.001

def calculate(aprox, iter):
    r = [0, 0, 0]
    for line_idx in range(0, len(matrix)):
        line_value = []
        div_value = 0.0

        partial_result = 0.0
        for column_idx in range(0, len(matrix[line_idx])):
            if column_idx == line_idx:
                line_value.append(0.0)
                div_value = matrix[line_idx][column_idx]
            else:
                line_value.append(matrix[line_idx][column_idx])

                #    partial_result -= (line_value[column_idx] * aprox[column_idx])

        # r[line_idx] = (results[line_idx] + partial_result) / div_value
        r[line_idx] = (results[line_idx] - (line_value[0] * aprox[0]) - (line_value[1] * aprox[1]) - (line_value[2] * aprox[2])) / div_value

    print("##### ITERACAO {} #####".format(iter))

    curr_error = 0.0
    for idx in range(0, len(aprox)):
        curr_error = max(abs(r[idx] - aprox[idx]), curr_error)

    if (abs(r[0] - aprox[0]) >= max_error) \
       or (abs(r[1] - aprox[1]) >= max_error) \
       or (abs(r[2] - aprox[2]) >= max_error):
        return calculate(r, iter + 1)
    else:
        return r

f = calculate(aprox, 0)

print("Valor final {}".format(f))
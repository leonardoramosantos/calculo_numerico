# # Exemplo 1 
matrix = [[10, 2, 1],
          [1, 16, 3],
          [1, 3, 10]]
results = [6, 8, 7]
aprox = [0.6, 0.5, 0.7]
max_error = 0.05

# # Exemplo 2
matrix = [[-4, 2, 1],
          [3, -4, 1],
          [15, 10, -31]]
results = [0, 0, 600]
aprox = [0, 0, 0]
max_error = 0.01


def calculate(aprox, iter):
    r = []
    for line_idx in range(0, len(matrix)):
        r.append(0.0)
        line_value = []
        div_value = 0.0

        partial_result = 0.0
        for column_idx in range(0, len(matrix[line_idx])):
            if column_idx == line_idx:
                line_value.append(0.0)
                div_value = matrix[line_idx][column_idx]
            else:
                line_value.append(matrix[line_idx][column_idx])

                if len(r) - 1 <= column_idx:
                    partial_result -= (line_value[column_idx] * aprox[column_idx])
                    # print("V", line_value[column_idx] * aprox[column_idx])
                else:
                    partial_result -= r[column_idx] * line_value[column_idx]
                    # print("V", r[column_idx] * aprox[column_idx])


        r[line_idx] = (results[line_idx] + partial_result) / div_value
        # print("LINHA", r[len(r) - 1])

    print("##### ITERACAO {} #####".format(iter))

    curr_error = 0.0
    for idx in range(0, len(aprox)):
        curr_error = max(abs(r[idx] - aprox[idx]), curr_error)

    if curr_error > max_error:
        return calculate(r, iter + 1)
    else:
        return r

f = calculate(aprox, 0)

print("Valor final {}".format(f))
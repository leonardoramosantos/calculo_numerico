# val_x = [1, 2, 3, 4]
# val_y = [2, 2, 4, 8]
# val_x = [25, 45, 65]
# val_y = [2350, 2200, 1850]
val_x = [1, 1.5, 2, 2.5, 3]
val_y = [66, 52, 18, 11, 10]
# val_x = [1, 2.5, 3]
# val_y = [66, 11, 10]

# final_array_1 = [-val_x[2] * -val_x[1], -val_x[2] * -val_x[0],
#                -val_x[1] * -val_x[0]]
# final_array_2 = [-val_x[2] + -val_x[1], -val_x[2] + -val_x[0],
#                  -val_x[1] + -val_x[0]]
# final_array_3 = [-val]


def dist_arrays(arr1, arr2=None):
    r = []

    if arr2 is None:
        r = arr1
    else:
        for idx_arr1 in range(0, len(arr1)):
            for idx_arr2 in range(0, len(arr2)):
                if (idx_arr1 == 0) \
                        or ((idx_arr1 == len(arr1) - 1)
                            and (idx_arr2 == len(arr2) - 1)) \
                        or ((idx_arr1 + idx_arr2) >= len(r)):
                    r.append(arr1[idx_arr1] * arr2[idx_arr2])
                elif idx_arr2 < (len(arr2) - 1):
                    r[idx_arr1 + idx_arr2] += (arr1[idx_arr1] * arr2[idx_arr2])

    return r


def quotients_array(arr1, div_number):
    r = []

    for n in arr1:
        r.append(n / div_number)

    return r


arr_xs = []
arr_x_div = []
arr_div = []

for idx_lagrange in range(0, len(val_x)):
    arr_loop_x = None
    loop_x_div = 1
    for idx_x in range(0, len(val_x)):
        if idx_lagrange != idx_x:
            arr_loop_x = dist_arrays([1, -val_x[idx_x]], arr_loop_x)
            loop_x_div *= (val_x[idx_lagrange] - val_x[idx_x])

    arr_xs.append(arr_loop_x)
    arr_x_div.append(loop_x_div)

    arr_div.append(quotients_array(dist_arrays(arr_loop_x, [val_y[idx_lagrange]]), loop_x_div))

answer = None
for arr_div_loop in arr_div:
    if answer is None:
        answer = arr_div_loop
    else:
        for i in range(0, len(arr_div_loop)):
            answer[i] += arr_div_loop[i]


print("Final", answer)

# v = dist_arrays([1, 2], [2, 4])
# print("partial", v)
# print("result", dist_arrays(v, [1, 3]))

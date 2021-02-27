def series(a, b):
    for i in range(a, b):
        for j in range(i, b):
                if i-a == j-i == b-j:
                    return a, i, j, b


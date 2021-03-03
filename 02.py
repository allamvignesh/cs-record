a, b = 0, 1

fibonacci = ()
for i in range(9):
    fibonacci += (a,)
    c = a+b
    a, b = b, c
print(fibonacci)

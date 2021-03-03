def unique(lst):
    fin = []
    for i in lst:
        if i not in fin:
            fin.append(i)
    return fin

for i in range(4):
    a = eval(input('Enter list: '))
    print(unique(a))

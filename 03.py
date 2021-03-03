dictionary = eval(input('Enter Dictionary: '))

a = list(dictionary.keys())

for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        print(a)

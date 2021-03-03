a = int(input('Enter the first number'))
b = int(input('Enter the second number'))

def check(x, y):
    x1 = int(x%10)
    y1 = int(y%10)

    return x if x1 < y1 else y

print(check(a,b))

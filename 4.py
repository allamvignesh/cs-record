from random import randint

def ran(n):
    start = 10**(n-1)
    end = (10**n) - 1

    return randint(start, end)

print(ran(1))

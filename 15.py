stack = [i for i in input('Enter string: ')]

while len(stack) != 0:
    c = stack.pop()
    if c == ' ':
        print(c,end='')
    else:
        print(c*2,end=' ')

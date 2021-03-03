stack = []
li = int(input('Enter limit: '))

s = input('P for push O for pop E for exit: ')

while s != 'e':
    if s == 'p':
        if len(stack) == li:
            print('stack is full')
        else:
            stack.insert(0,int(input('Enter element')))
    elif s == 'o':
        if len(stack) < 1:
            print('stack is empty')
        else:
            stack.pop(0)
    print(stack)
    s = input('P for push O for pop E for exit: ')

print(s)

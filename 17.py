li = int(input('Enter limit: '))

queue = ['' for i in range(li)]
f,r = -1,-1

s = input('I for insert D for delete E for exit: ')

while s != 'e':
    if s == 'i':
        if r == li-1:
            print('Overflow')
        else:
            r+=1
            queue[r] = int(input('Enter element: '))
            if f == -1:
                f = 0
    elif s == 'd':
        if (f == r == -1):
            print('Underflow')
        else:
            queue[f] = ''
            if f == r:
                f,r = -1,-1
            else:
                f += 1
    print(queue)
    s = input('I for insert D for delete E for exit: ')
            
            
            

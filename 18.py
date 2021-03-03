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
            e = input('R for rear end F for front end: ')
            if e == 'f':
                queue[f] = ''
                if f == r:
                    f,r = -1,-1
                else:
                    f += 1
            elif e == 'r':
                queue[r] = ''
                if f == r:
                    f,r = -1,-1
                else:
                    r -= 1
                
    print(queue)
    print(f,r)
    s = input('I for insert D for delete E for exit: ')
            
            
            

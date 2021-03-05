global li
li = int(input('Enter limit: '))

HighestPr = ['' for i in range(li)]
NormalPr = ['' for i in range(li)]
LowerPr = ['' for i in range(li)]

hf = hr = -1
nf = nr = -1
lf = lr = -1

s = 0

def insert(e, f, r, queue):
    if r == li-1:
        print('Overflow')
    else:
        r+=1
        queue[r] = e
        if f == -1:
            f = 0
    return (f,r)

def search(e):
    if e in HighestPr:
        return 'HighestPr'
    if e in LowerPr:
        return 'LowerPr'
    if e in NormalPr:
        return 'NormalPr'
    return 'Element not found'

def delet(p,e):
    if p == 'H':
        i = HighestPr.index(e)
        del HighestPr[i]
        HighestPr.insert(0,'')
    elif p == 'N':
        i = NormalPr.index(e)
        del NormalPr[i]
        NormalPr.insert(0,'')
    elif p == 'L':
        i = LowerPr.index(e)
        del LowerPr[i]
        LowerPr.insert(0,'')




while s != 4:

    print('1.Insert Element\n2.Search for Element\n3.Change Priority\n4.Exit')

    s = int(input('select option: '))

    if s !=4:
        e = input('Enter element : ')

    if s == 1:
        p = input('Priority (Highest/ Normal/ Lower(H/N/L)): ')
        if p == 'H':
            hf, hr = insert(e, hf, hr, HighestPr)
        if p == 'N':
            nf,nr = insert(e, nf, nr, NormalPr)
        if p == 'L':
            lf, lr = insert(e, lf, lr, LowerPr)
    elif s == 2:
        print(search(e))
    elif s == 3:
        p = search(e)[0]
        if p != 'E':
            todo = input('Want to increase/Decrease its priority(I/D): ')
            if todo == 'I':
                if p == 'N':
                    delet(p,e)
                    hf,hr = insert(e, hf, hr, HighestPr)
                if p == 'L':
                    delet(p,e)
                    nf, nr = insert(e, nf, nr, NormalPr)
            elif todo == 'D':
                if p == 'H':
                    delet(p,e)
                    nf,nr = insert(e, nf, nr, NormalPr)
                if p == 'N':
                    delet(p,e)
                    lf, lr = insert(e, lf, lr, LowerPr)
    print(HighestPr,NormalPr,LowerPr)

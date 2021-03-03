def unique(lst):
	un = []
	qw = []
	for i in lst:
		un.append(lst.count(i))
	for i in range(len(un)):
		if un[i] == 1:
			qw.append(lst[i])
	return qw
 
for i in range(4):
    a = eval(input('Enter list: '))
    print(unique(a))

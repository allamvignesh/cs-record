def MVisit(lst):
	mx = 0
	for i in range(len(lst)):
		if len(lst[i]) > len(lst[mx]):
			mx = i
	return lst[mx]

V = eval(input('Enter details: '))
print(MVisit(V))

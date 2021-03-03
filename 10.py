f = open('Article.txt', 'r')

a = f.readlines()
count = 0

'''lines = [i.split('. ') for i in a]

for line in lines:
    for senten in line:
        if senten[0] == 'A':
            count += 1
'''
for i in a:
	if i[0] == 'A':
		count += 1
f.close()
print(count)

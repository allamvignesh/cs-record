f = open('Article.txt', 'r')

a = f.readlines()
lines = [i.split('. ') for i in a]
count = 0

for line in lines:
    for senten in line:
        if senten[0] == 'A':
            count += 1

f.close()
print(count)

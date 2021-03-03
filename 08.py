f = open('Article.txt', 'r')

lines = f.read()
count = 0

for letter in lines:
    if letter.isupper():
        count += 1

print(count)

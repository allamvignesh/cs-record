f = open('Article.txt', 'r')

lines = f.readlines()
count = 0

for line in lines:
    for word in line:
        for letter in word:
            if letter.isupper():
                count += 1

print(count)

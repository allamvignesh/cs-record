low = open('lower.txt', 'w')
up = open('upper.txt', 'w')
other = open('others.txt', 'w')

run = True
while run:
    character = input('Enter char: ')
    if character == 'quit':
        run = False
    elif character.islower():
        low.write(f'{character}\n')
    elif character.isupper():
        up.write(f'{character}\n')
    else:
        other.write(f'{character}\n')

low.close()
up.close()
other.close()

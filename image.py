from client import client

conn = client()
print(conn.send(input('Name: ')))
a = open('a.png', 'rb')

b = a.readlines()
while True:
    print('yey')
    server = conn.send(b)
    print(server)

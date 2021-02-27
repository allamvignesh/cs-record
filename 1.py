inp_date = int(input("Enter date(MMDDYYYY) : "))

Month = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

month = Month[inp_date//1000000]
inp_date %= 1000000
date = inp_date//10000
inp_date %= 10000
year = inp_date

print(f'{month} {date}, {year}')

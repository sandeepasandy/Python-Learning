'''
import random
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#ascii_letters--This string module function that can give
upper and lower letters
#digits--This string module function that can give numbers(0-9)
#punctuation--This string module function can give us
punctuation (&$@)

import random
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all_chars = letters + digits + punctuation

password = ''
for i in range(7):
    password += random.choice(all_chars)

print(password)

--for getting special characters:
eg:
import random
import string

letters = string.ascii_letters
digits = string.digits
special_char = '@#$*'

all_chars = letters + digits + special_char

password = ''
for i in range(7):
    password += random.choice(all_chars)

print(password)

bank_balance = 30000
from datetime import datetime
import sys
now = datetime.now()

while True:
    print("----Welcome to SBI ATM----")
    user_opt = int(input("\n1.Withdraw \n2.Deposit \n3.check balance \n4.exit:"))
    if user_opt == 1:
        With_m = int(input('Enter the money you want to withdraw'))
        if With_m > bank_balance:
            bank_balance -= With_m
            print(f'remaining money {bank_balance} {now.strftime} ("%H:%M %Y-%m-%d")')
        else:
            print("Insufficient balance")
    elif user_opt == 2:
        Deposit_m = int(input('Enter the money to deposit'))
        bank_balance += Deposit_m
        print(f'Money added successfully: {bank_balance} {now.strftime} ("%H:%M %Y-%m-%d")')
    elif user_opt == 3:
        print(f'Available balance: {bank_balance} {now.strftime} ("%H:%M %Y-%m-%d")')
    elif user_opt == 4:
        sys.exit()
    else:
        print("incorrect choice")
        print("Thank you for visting the ATM")
        sys.exit()
'''
import random
num = random.randint(1,100)
user_opt = int(input("Pick a number(1-100): "))
if user_opt == num:
    print(f'You have picked {user_opt} number')
else:
    print('Better luck next time')
                   




























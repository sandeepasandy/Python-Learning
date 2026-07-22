'''Output Formatting
1.Comma Separation(,):
name='Sandy'
age = 21
print('Welcome ',name,'Your age is',age)
2.F-string(doc-string)
name='Sandy'
age = 21
print(f'Welcome {name}Your age is {age}')
3.Modules:
%s:For string,int and all
eg:
name = 'sandy'
print('name : %s' %name)
%d:for digit
eg:
price = 89
print('name :%d' %price)
%f:for float (56.9)
eg:
price = 89
print('name :%f' %price)
4.(dot) .format()
eg:
name = 'sandy'
age = 21
print('name :{} \nage : {}'.format(name,age))
------STATEMENTS:
1.CONDITIONAL STATEMENTS:
if,if-else,else-if,nested-if
2.CONTROL STATEMENTS:
break,continue,pass
3.LOOP:
while,for

if condition:
age=int(input("Enter your age: "))
if age >= 18:
    print(f"your age is {age} and eligible to  vote")

if-else condition:else is the fall back statement,incase if condition is false then the
else block will execute
ex:
age=int(input("Enter your age: "))
if age >= 18:
    print(f"your age is {age} and eligible to  vote")
else:
    print(f"your age is {age},you have to wait {18 - age} years")
ex2:
num = int(input("enter a number: "))
if num % 2 == 0:
    print(f'{num} is a even number')
else:
    print(f'{num} is a odd number')
ex3:
vol_ = input('Enter a single letter: ')
if vol_ in 'AEIOUaeiou':
    print(f'{vol_} is a Vol')
else:
    print(f'{vol_} is a consonant')
ex3:
so = 'python'
do = so[::-1]
print(do)
if so[::-1] == so:
    print(f'{so} is a pali')
else:
    print(f'{so} not a pali')
ex4:'''
year_ = int(input('Enter a year: '))
if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
    print(f'{year_} is a leap year')
else:
    print(f'{year_} not a leap year')



'''Statements
1.Else if:
ex:
marks_ = int(input("Enter your Marks: "))
if marks_ > 90:
    print('A+')
elif marks_ >= 80:
    print('A')
elif marks_ >= 70:
    print('B')
elif marks_ >= 60:
    print('B+')
elif marks_ >= 50:
    print('C')
elif marks_ >= 40:
    print('C+')
else:
    print('fail')
ex2:
num = 89
num_2 = 102
num_3 = 5
if num > num_2 and num > num_3:
    print(f'{num} is greater value')
elif num_2 > num and num_2 > num_3:
    print(f'{num_2} is greater value')
else:
    print(f'{num_3} is greater value')
2.Nested if:
if first condition executed then only it go inside.if first
condition not executed then it will not go inside.
details_={'ATMPIN': '1212'}

atm_ = input('enter 4 digit atm pin: ')
if len(atm_) == 4:
    if atm_ == details_['ATMPIN']:
        op_ = int(input("Enter \n1.Withdraw \n2.Deposite \n3.Pinchange"))
        if op_ == 1:
            Money_W = int(input('Enter money to withdraw: '))
        elif op_ == 2:
            Money_D = int(input('Enter money to Deposite: '))
    else:
        print('Incorrect pin Entered')
else:
    print('please enter only 4 digit pin')
3.Break condition:
ex:
num = [24,36,78,45,90]
for i in num:
    print(i)
    if i == 78:
        break
else:
    print('end')
4.Continue:Skips the particular iteration
Ex:
num = [24,36,78,45,90]
for i in num:
    print(i)
    if i == 78:
        continue
else:
    print('end')
5.Pass:
--Space holder
--if a statement is incomplete if we put pass after that no error will be raised
ex:'''
num = [24,36,78,45,90]
for i in num:
    pass
'''>>>Loops:
6.for loop:
--for loop is used to itterate over sequence such as string,List,tuple,
--else in for loop it will execute when whole itterates are completed.
--incase if condition becomes true, then else will never execute.
num = 'Python is a language'
for i in num:
    print(i)
    if i == 'a':
        break
else:
    print('end')
--range():range is a function where it give the sequence of numbers
--this function is used to generate number upto a limit
--Syntax:range(start,end,step)
ex:
for j in range(1,10,3):
    print(j)
7.While Loop:
ex:
num = 6
while num < 20:
    print(num)
    num += 1
Assert keyword:
--the keyword is used to check the condition
eg:
age = 13
assert age>=18, 'Not eligible'
print('eligible')
eg2:'''
Marks_ = 67
assert Marks_ >= 35, 'Fail'
print('Pass')  

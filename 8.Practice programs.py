'''1.Even number odd number
limit_=int(input('Enter the limit: '))
for j in range(1,limit_+1):
    if j % 2 == 0:
        print(f'{j} is a even')
    else:
        print(f'{j} is a odd')
2.Prime number or not prime:
num = int(input('Enter a num: '))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
    print(f'{num} is prime')
else:
    print(f'{num} is  not a prime')
3.Prime number example2:
for i in range(2,10):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
        if count == 2:
            print(f'{i} is a prime')
4.string reversal:
rev_ = input('Enter a word: ')
emp_ = ''
for j in rev_:
    emp_ = j + emp_
if emp_ == rev_:
    print(f'{rev_} is a palindrome')
else:
    print(f'{rev_} is not a palindrome')
5.
*
**
***
****
star_=int(input('Enter a num: '))
for j in range(1,star_+1):
    for i in range(1,j+1):
        print('*',end='')
    print()
6.
1
12
123
1234
star_=int(input('Enter a num: '))
for j in range(1,star_+1):
    for i in range(1,j+1):
        print(i,end='')
    print()
7.
1
23
456
78910
count = 0
star_=int(input('Enter a num: '))
for j in range(1,star_+1):
    for i in range(1,j+1):
        count += 1
        print(count,end='')
    print()  
8.Pyramid:
num = 7
for j in range(num):
    print(" " * (num -j -1),end = '')
    print('* ' * (j+1))
9.reverse pyramid:
num = 10
for j in range(num,0,-1):
    print(" " * (num -j),end = '')
    print('* ' * j)
10.
nums = [1,2,2,5,5]
emt_ = []
for j in nums:
    if j not in emt_:
        emt_.append(j)
print(emt_)
11.Perfect number:
num = int(input('Enter a number: '))
per_num = 0
for j in range(1,num):
    if num % j == 0:
        per_num += j
if per_num == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')


















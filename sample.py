'''1.Print
*
****
**
star_= [1,4,2]
for i in star_:
    for j in range(i):
        print('*',end=" ")
    print()
1.Check whether a number is postive or negative
n=int(input('Enter a number: '))
if n > 0:
    print('Postive number')
elif n < 0:
    print('Negative number')
2.check given string is palindrome or not
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")
3.print:011235813
4.check age and return true if age is less than 55
age=int(input('Enter the age: '))
if age <= 55:
    print('True')
else:
    print('False')
5.print if city=vizag then "A"
if city = vijayawada then "B"
if city = vizag&vijayawada print "C"
if city!= vizag & vijayawada print "D"
city=input("Enter a City: ")
if city == Vizag:
    print("A")
elif city == Vijayawada:
    print("B")
elif city == Vizag&Vijayawada:
    print("C")
else city != Vizag&Vijayawada:
    print("D")





Practice Programs:
1.
n=int(input('Enter a number: '))
if(n%2==0):
    print('Even number')
else:
    print('Odd number')
    
2.
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("not a Palindrome")

3.
def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Number of vowels:",
      count_vowels(string))
    

31-07-2026

a=5
b=3
print("5&3= ",a&b)
c=6
d=9
print("6&9= ",c&d)

name=input("Enter your Name: ")
for i in range(1515):
    print(name)

for i in range(4):
    print("***")
    
num=int(input('Enter a Number: '))
prime = True
if num <= 1:
    prime = False
else:
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break

rev=int(str(num)[::-1])

if prime:
    print("Prime number")
else:
    print("Not a prime number")
if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
if prime and num == rev:
    print("It is both prime & Palindrome")


s =input("Enter a number: ")
f= float(s)
print("Float value:",f)

6-08-26
name=input("Enter your name: ")
age=int(input('Enter your age: '))
print(f"Hello, {name}! you are {age} old. WELCOME!")

names = ['Priya','Ajay','Raju','John','Ashok']
for name in names:
    if name[0] == 'A':
        print(name)

n=int(input('Enter a number: '))
if(n%2==0):
    print('Even number')
else:
    print('Odd number')

days = int(input("Enter the number of days: "))
'''
'''
07-08-26

print("Hello, World!")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(num1 + num2)

n = int(input("Enter the length of the rectangle: "))
n2 = int(input("Enter the width of the rectangle: "))
Area = n * n2
print("The area of rectangle is:", Area)

name = input('Enter your name: ')
age = int(input("Enter your age: "))
print(f"Welcome! {name} your age is {age}") 

n=int(input("Enter a number: "))
if n%2==0:
    print("Even number")
else:
    print("Odd number")


numbers = [10, 25, 5, 40, 15]
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum:", maximum)
print("Minimum:", minimum)

any_ = ['Python is a good language']
print(any_.count('10'))

OOPs Concepts:
class Student:
    name = 'sandeepa'
    age = 21
    Grades = 'A'
s = Student()
print(s.name)
print(s.age)
print(s.Grades)
'''
class CSV_file:
    name = 'John'
    position = 'Trainer'
    salary = 30000
Employee_ = CSV_file()
print(Employee_.name)
print(Employee_.position)
print(Employee_.salary)
    





























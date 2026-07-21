'''Input Formatting:
Int()=input formatting for the integer int(input())
eg:
num=int(input('enter a num:'))
print(num+9)
print(type(num))

String()=input formatting for string input()
eg:
we=input('enter: ')
print(type(we))

List:
nums = list(map(int,input('Enter nums: ').split()))
print(nums)

for string:
nums = input('Enter nums: ').split()
print(nums)

Tuple:
nums = tuple(map(int,input('Enter nums: ').split()))
print(nums)

Without this mapping
nums = eval(input("Enter:"))
print(type(nums))

Task:24hrs clock into 12hrs clock
time_=input("Enter 24H clock: ")

parts_=time_.split(':')
Hours_=int(parts_[0])-12
print(Hours_,':',parts_[1],'pm')'''

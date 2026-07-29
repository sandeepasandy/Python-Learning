'''Default Arguments:
ex:
def any_(name,edu,age):
    print(age)
any_('Sandy',21,'B.Tech')

def any_(name,edu,age):
    print(age)
    print(name)
any_(name='Sandy',age=21,edu='B.Tech')

Variable-length positional arguments:
--* means args
--we can pass tuple of arguments and stored in a single parameter by just
adding * before the parameter
--and we can access the arguments using indexing
ex:
def all_va(*nums):
    print(nums[1] + nums[3])
all_va(10,34,5,89)
Variable-length keyword arguments:
--**kargs
--By passing keyword arguments in the arguments,will get it as dictionary
just adding ** before the parameter
--and can access by using dictionary methods..
Eg:
def dct(**all_in):
    for key, val in all_in.items():
        print(key,':',val)
dct(name = 'sandy',age=21, role = 'Trainee')
eg2:
def dct_nums(*args,**kargs):
    print(args)
    print(kargs)
dct_nums(12,56,7,name='sandy',age=21,edu='B.Tech')
--**kargs should not use before it will be an error
def dct_nums(**kargs,*args):
     print(args)
    print(kargs)
dct_nums(12,56,7,name='sandy',age=21,edu='B.Tech')
Scope of variables:
eg:
num_2 = 89
def nums(num_2):
    num =90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)

limit_ = int(input('Enter the limit: '))
num = 0
num_2 = 1

def fibonacci(limit_,num,num_2):
    print(num,num_2, end=' ')
    for j in range(1,limit_+1):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
fibonacci(limit_,num,num_2)

Passing by values:
--passing direct values in the arguments
eg:
def any_(a,b):
    print(a)
    print(b)
any_(8,56)
Passing by reference:
eg:'''
def any_(num,num_2):
    print(num)
    print(num_2)
any_(num = 8,num_2 = 9)


    





























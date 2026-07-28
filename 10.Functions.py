'''Functions:
--function is block that can be executes when we call it.
--To avoid the repeated lines if codes
def function_name(parameters):
 ---------
 ---------
 ---------
function_name(arguments)

Types of functions:
1.Bulit_in
eg:
print()
len()
max()
min()

2.User-define:
--User define are the functions that are develop by the user
#addition
num=56
num_2=89
def total(num,num_2):
    print(num+num_2)
total(num,num_2)
total(1,2)

#subtraction:
num=56
num_2=76
def total(num,num_2):
    print(num-num_2)
total(num,num_2)
total(5,3)

#Multiplication:
num=56
num_2=76
def total(num,num_2):
    print(num*num_2)
total(num,num_2)
total(5,3)

Required arguments"
--we have to pass same number arguments that match in the parameters
eg:
num=56
num_2=89
def total(num,num_2):
    
    print(num + num_2)
    
total(num,num_2)
total(1,2,3)#error

Positional arguments:
--it does not matter how we are passing the variable,if we assign the
value to that variable in the calling

eg:
def Name_(name_,name):
    print(name)
    print(name_)
Name_(name = 'sandy',name_ = 'sandeepa')

eg2:'''
def pos_(m,d,a,c,b):

    print(pos_)

pos_(a=0,b=8,c=4,d=1,m=7)

















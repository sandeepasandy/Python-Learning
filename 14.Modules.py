'''Modules:
Modules are the python code which is saved in (.py) that contains
functions,variables,classes

type:
1.built-in:The built in modules that are already designed which
comes with python when we are installing
eg:
1.math
2.sys
3.os
4.random


2.User defined:The user defined modules are created by the programmer
syntax:
import(keyword) module_name

import first_module

print(first_module.add(56,8))
print(first_module.subtract(67,8))
print(first_module.mul(5,9))
print(first_module.div(54,8))

importing with alias name:
--we can also import a module with different name
--after importing with the alias name ,we have to use the alias
name in the code
ex:
import first_module as fm

print(fm.add(56,8))
print(fm.subtract(54,7))

importing only needed functions:
--when we importing the few functions from the module
can only access that function
syntax:
from(keyword) module_name import (keyword) functions
eg:
from first_module import add,mul

print(add(56,4))
print(mul(14,5))

importing all functions:
use the all functions in the module we have to use(*)
to get all of these
syntax:from(keyword) module_name import(keyword)*)

from first_module import *
print(add(56,4))
print(subtract(41,51))
print(mul(15,4))
print(div(56,4))


import first_module

first_module.display()

built in examples:

random:
import random
print(random.randint(1000,9999))

math:
import math
print(math.sqrt(25))

sys:
import sys
print(sys.version)

'''
details ={
    'name' : 'sandy',
    'ATM PIN' : '1212'
}
import random

remain_ = 3
while remain_ > 0:
    pin_ = input('Enter pin number: ')
    if pin_ == details['ATM PIN']:
        otp = random.randint(1000,9999)
        print(otp)
        user_otp = int(input('Enter user otp: '))
        if user_otp == otp:
            otp = int(input('Enter option \n1.withdraw \n2.deposit'))
        else:
            remain_ -= 1
            if remain_ > 0:
                print(f"incorrect pin entered and you have {remain_}")
            else:
                print(f"you have entered 3 times incorrect pin card blocked")

























'''Anonymous function:
--anonymous function is a function that don't any name
--This also called as lambda function
--Lambda function will take n number arguments but only one expression
Syntax-->lambda arguments:expression

map():
The map function will be applied on the given function of each and every
element of an iterable
ex:
nums = [1,2,3,4,5]
so=list(map(lambda x: x*x,nums))
print(so)

filter():
--filter function will only consider if the condition is true,then
it will keep that values..
ex:
nums = [1,2,3,4,5]
so=list(filter(lambda x: x%2==0,nums))
print(so)

reduce():
--the reduce() function consider all elements and reduce to one single element
--To use this reduce() we have to import it first from the functools
eg:
from functools import reduce
nums =[1,2,3,4,5]
so = reduce(lambda x,y : x+y,nums)
print(so)

print():
--print() is an in-bulit function that is used for the display the
values stored by variable

return:
--Only used inside the functions
--When the return is executed then it exit from that function
and holds the returned values in the calling


























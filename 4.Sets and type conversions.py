'''SET:
Set is an unordered collection
set do not allows duplicate values inside it
set is a muttable datatype
set is represented in{}
ex:
do={1,2,3}
print(do)
o/p:{1,2,3}
--Creating an empty set
so=set()
print(type(so))
o/p:<class 'set'>
--Methods
1.Update:
used to add new value in a set
syntax:variable_name.update(iterables)
ex:
so={1,2,3}
so.update('python')
print(so)
o/p:{1,2,3,'o','y','p','t','n','h'}
2.add()
used to add new value into set
syntax:variable_name.add(values)
ex:so={1,2,3}
so.add(4)
print(so)
o/p:{1,2,3,4}
3.Remove()
used to del the value from the set,incase if the value is nor present in the set
will get the key error
syntax:variable_name.remove(value)
ex:so{1,2,3}
so.remove(4)
print(so)
keyerror:4
2nd ex:
so={1,2,3}
so.remove(3)
o/p:{1,2}
4.Discard()
unlike remove method if the value is not present in the set it wont
throw the key error
syntax:variable_name.discard(value)
ex:so={1,2,3}
so.discard(3)
print(so)
o/p:{1,2}
5.pop()
used to del the value but this po() will take 0 argumnets inside it and inside the function
no need to mention anything or else we will thrown with a positional arguments error
Syntax:variable_name.pop()
ex:s0={1,2,3}
so.pop()
print(so)
o/p:{2,3}
    OPERATIONS
--UNION:maps two sets together with a single frequency of each item
it is denoted by | or syntax:variable_1.union(variable_2)
ex:
do={3,4,5}
so={1,2,3}
print(so|do)
o/p:{1, 2, 3, 4, 5}
ex:
do{3,4,5}
so={1,2,3}
print(so.union(do))
o/p:{1, 2, 3, 4, 5}
--Intersection:common values among sets
syntax:variable_1.intersection(variable_2)
ex:
do={3,4,5}
so=[1,2,3]
print(do&so)
print(do.intersection(so))
--Difference:
ex:
do={3,4,5}
so=[1,2,3]
print(do-so)
print(do.difference(so))
                TYPE CONVERSIONS
--Int:
--String=str()
eg:
num=9
print(type(num))
so = str(num)
print(type(so))

--Float=float()
eg:
num=9
print(type(num))
so = float(num)
print(so)
print(type(so))

--Float:
String=str()
nums=8.67
print(type(nums))
all_=str(nums)
print(type(all_))

Integer ---int()
nums=8.67
print(type(nums))
all_=int(nums)
print(all_)
print(type(all_))

String()
Integer=int()
eg:
Can't convert
how="I have 67 Rupp"
print(type(how))
who = int(how)
print(type(who))

Can convert
how="67"
Print(type(how))
who = int(how)
print(type(who))


Float--float()
how="6.87"
Print(type(how))
who = float(how)
print(type(who))

List:
how='2345'
Print(type(how))
who = list(how)
print(who)
print(type(who))

tuple--tuple()

how='2345'
Print(type(how))
who = tuple(how)
print(who)
print(type(who))

String=str()
tuple=tuple()
ex:
nums=[1,2,3,4]
print(type(nums))
all_n=str(nums)
print(type(all_n))

tuple=tuple()
nums=[1,2,3,4]
print(type(nums))
all_n=tuple(nums)
print(all_n)
print(type(all_n))

tuple
list eg:
nums=[1,2,3,4]
print(type(nums))
all_n=list(nums)
print(all_n)
print(type(all_n))
tuple string eg:
nums=(1,2,3,4)
print(type(nums))
all_n=str(nums)
print(type(all_n)

(+)concatenation
num=8
num_2=9
print(num+num_2)

any_='Python is a'
we = ' Language'
print(any_+ we)
list concatenation:
nums = [1,2]
all_= [3,4]
print(nums+all_)
Tuple concatenation:
nums = (1,2)
all_= (3,4)
print(nums+all_)'''
    


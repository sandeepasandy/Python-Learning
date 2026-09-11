'''---Tokens:
-->Tokens are smallest individual parts or units in the program
--key words:
----keywords are the reserved words

if
while
else
return
for
and
in
identifiers:
---variable
function name
class name
operators:
+ - =
4.literal:
int,str,tuple,list

Operators:
   1 arithmetic operator:+,-,*,%,**
   2 Assignment operator
    =,+=,-=,*=,%=,/=
   3 comparision
    ==,!=,<=,>=,>,<
    4 logical
    and or not
    5 identity
    is isnot
    is look for object
    == checks the values are same or not
    6 membership
    in not in
    7 bitwise
    &,|,^,<<,>>


num=9
num_2=7
print(num + num_2)
print(num - num_2)
print(num * num_2)
print(num ** num_2)
print(num % num_2)
print(num / num_2)
'''
num=8
num_2=6
print(num == num_2)
print(num != num_2)
print(num > num_2)
print(num < num_2)
'''
num=78
num_2=89
print(num<num_2 and num_2<100)
print(num>num_2 or num_2<100)
print(not(num<num_2 and num_2<100))

num=9
num_2=9
print(num is num_2)
print(num == num_2)

so=[1,2,2,4,5,]
print(7 in so)
print(7 not in so)

print(5 & 3)
print(5 | 3)
print(5 << 3)
print(5 >> 3)

Datatypes: To find datatype we should use this syntax type(variable_name)
To find memory id(variable_name)
Integer:
integer nothing but numbers
number=9
Can perform arithmetic operations
Float:
num=89.45
print(type(num))
String:
    string is a sequence of characters that are enclosed in (' ',"",''',''')
    the characters given in those quotes then it is called as string
    string is immutable
    so='python is a language'
    for j in so:
        print (j)
Method:
    Replace():Used to replace old string with new string
    syntax:variable_name.replace('old_str','new_str','how many')
    how many is an optional

so='python is a language python python'
print(so.replace('python','java'))

    Join():This method will add new char after every substring
    Syntax:'new_string'.join(variable_name)
so='python is a language'
print('-'.join(so))

    Split():
so='python is a language'
print(so.split('is'))
    Index():gets the position value
so='python is a language'
print(so.index('a'))
    Count:counts the variable place
so='python is a language'
print(so.count('n'10,16))
   Indexing:will give what we give to find a index integer
so='python is a language'
print(so[12])

  List:
      list is a collection of different datatypes that are represented
      in square brackets and separated by ,
      list is a muttable datatype
any_=[1,'python',[2,['python',9],4],'java',['python',[56,78],'java',90]]
print(any_[4])
 Append:
 Append method is used to add new item into the list and it will add at
last index position
any_=[1,2,3,4,5]
any_.append([10])
print(any_)

Extend:
any_=[1,2,3,4,5]
any_.append("python")
print(any_)
any_.extend("python")
print(any_)

Remove:
remove will delete the item based on the value given
if the value not the list will the error
any_=[1,2,3,4,5,2]
any_.remove(2)
print(any_)

Pop:
the pop will delete the item based on the index position given
if the index position is out of  range in the list will the error
any_=[1,2,3,4,5]
any_.pop(2)
print(any_)'''



      
      

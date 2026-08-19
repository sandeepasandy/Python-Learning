'''Regular Expression (RegEx)
--This RegEx is used to form a search pattern to find of the string contain
sequence char or not
--To use this RegEx, we need to import re module

Functions:
Findall:
--The searching pattern is found then,it will gives the output
in the list[]

eg:
import re
Some = 'Python is a programming language'
print(re.findall('[a]',Some))

--Here in this example the findall is used to find the 'a' elements
in the list

Search
--This is also used to form a search pattern,but it will give only
the first matched object
--Where it will gives with the index position,where the matched object
is found by the pattern

ex:
import re
do = 'I have 1000 ruppees with me'
print(re.search('e',do))

--In this search option the we gave the program to find the 'e' elemnts
so it will give the index positions

Meta characters:
--Meta characters are the symbols used in the search pattern
1)[]

--This [] symbol is used to find a group char that present in the string,
where we can also specify the range
syntax--> re.findall('[range]',variable_name)
--by using this symbol we can search cap(A-Z),small(a-z)
and digit(0-9)
ex:
import re
some = '12 We are Doing Fun and we are So HAppy'
print(re.findall('[arod]',some))
print(re.findall('[a-z]',some))
print(re.findall('[A-Z]',some))
print(re.findall('[0-9]',some))
print(re.search('[a-z]',some))

--In this program findall will find all the elements
wheras search will find only particular character

2).
--This symbol will refer only one character means can match only
a single character in the pattern
syntax-->re.search('C...',variable_name)
ex:
import re
some = 'Hello! World'
print(re.findall('H...o',some))
print(re.search('H...',some))

3)+
--The symbol can find max number of sequence from the string from
atleast one character
--Syntax--re.findall('.+',variable_name)
ex:
import re
some = 'Not an Indian number'
print(re.findall('N.+n',some))

4)^
--This symbol is used to find the pattern where string is
starting with match or not
--Syntax--re.findall('^',variable_name)
ex:
import re
some = 'Hello! World'
print(re.search('^H',some))
print(re.findall('^Hello',some))

5)$
--This symbol will find out if the string is ending with the pattern or not
--Syntax--re.findall('sequence$',variable_name)
ex:
import re
any_ = 'I am planning for a trip'
print(re.findall('for a trip$',any_))
print(re.search('for a trip$',any_))

6)?
--The symbol will find max upto one match in the string
syntax--re.findall('.?',variable_name)
eg:
import re
some = 'Hello! World Hello'
print(re.findall('Hel.?o',some))

7)*
--The symbol findouts max number of sequence from the string
--syntax--re.findall('.*',variable_name)
ex:
import re
some = 'Not an Indian number'
print(re.findall('N.*n',some))

8){}
--The symbol is used to find a group char that present in string
syntax--re.findall('E.{size}',variable_name)\
ex:
import re
all_ = 'I have 1000 ruppees with me'
print(re.findall('I.{4}',all_))

ex2:
import re
user_name = input("Enter your name:")
pattern = re.search('^[A-Z,a-z]{3,}$',user_name)
if pattern:
    print('Correct')
else:
    print('Incorrect')

ex3:
import re
num = input("Enter your number:")
find = re.findall('^[6-9][0-9]{9,}$',num)
if find:
    print('Indian number')
else:
    print('Not an Indian number')
'''
import re
some = 'The Not an Indian number'
print(re.findall('T.+he',some))
print(re.findall('T.*he',some))



















































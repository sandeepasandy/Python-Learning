'''1.Tuple:
Tuple is acollection of different datatype that are represented in
()paranthesis and separated by,
Tuple is immuttable
-Methods:
index:syntax--variable_name.index(item)
ex:
go=(1,'java',[3,4],('python',78))]
print(go.index('java'))
-count:
syntax--variable_name.count(item)
go=(1,'java',[3,4],('python',78))]
print(go.count('python',78)))---o/p-->1
print(go.count('python'))---o/p-->0
2.Dictionary:
Dict is a key:value pair
keys and values separated by :
dict is represented by{}
keys must be immuttable datatypes
-Methods:
-keys:
syntax:dict.keys()
-values:
syntax:dict.values()
-items:
syntax:dict.items()
-Update:
syntax:dict.update({key:value})
Details.update({'gender':'female'}) or
-clear:
syntax:dict.clear()'''
Details={'name':'sandy',
         'AC':12345,
         'pan':445214,
         'pin':1212}
Details.update({'gender':'female'})
print(Details.values())
print(Details.keys())
print(Details.items())
print(Details.clear())

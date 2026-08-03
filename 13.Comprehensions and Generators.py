'''List comprehension:
--The list comprehension is the short form of syntax used to
generate a new list from the old list..
syntax--[expression loop]

nums = [1,2,3,4,5]
new_l = [j if j%2 == 0 else 'odd' for j in nums]
print(new_l)

nums = [1,2,3,4,5]
nel_ = [i for i in nums if i % 2 != 0]
print(nel_)

Nested comprehension:
--Nested comprehension means a comprehension inside the another comprehension
is called nested comprehension
syntax--[expression loop_1 and loop_2]
match=[[1,2,3],
       [4,5,6],
       [7,8,9]
       ]
any_ = [i for i in match]
all_ = [num for j in match for num in j]
print(any_)
print(all_)
ex2:
new_ = [[i*j for j in range(1,6)] for i in range(1,6)]
ne = [i for i in range(1,6)]
print(ne)
print(new_)

Generators:
--This Generator will generate one values at a time and pause
it on the same position when we are using yield keyword 
--It is also called as lazy evaluation
--Here we will use yield to get the value

yield() Keyword:
--This yield() is used to get the values and will
only gives one value and pauses there itself

next() keyword:
--The next() keyword will retrieve the value

ex:
def gen(n):
    for i in range(1,n+1):
        yield i*i
a = gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

Function:                                    
--return                                     
--When the function is executed ,it
will exit from the function\
--In function will get all values once                                     

Generator:
--yield
--When the yield is executed,it will pass
the function and the next yield is called
then it will resume again
--In Generation will get one at a time.
                                   






























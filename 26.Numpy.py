'''Data Analysis:
Data analysis is the process of collecting,cleaning,transforming,organising
and analyzing data to convert into useful information and also used for making decisions
to get the better outcome...

Libraries used:
Numpy
Pandas
matplotlib
seaborn

Numpy:
--This refers to numerical python,
--It is an Python library used for calculations and operations
--This Python library is more faster then the list to perform operations
--And also this supports Multi-dimensional arrays

ex:(single-dimensional array)
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)

ex2:(two dimensional array)
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.ndim)
arr_3 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr_3.ndim)

ex3:By adding [] to the list i can become 3-dimensional
import numpy as np
arr_2 = np.array([[1,2,3,4,5]])
print(arr_2.ndim)
arr_3 = np.array([[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]])
print(arr_3.ndim)

import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.shape)
arr_3 = np.array([
    [1,2,3],
    [4,5,6],
])
print(arr_3.shape)

Functions:
1)ndim:
--The function is used to find out the dimensions of an array
Syntax--array.ndim
eg:
import numpy as np
arr_2 = np.array([[1,2,3,4,5]])
print(arr_2.ndim)

2)shape:
--The shape function is used to find the rows and columns of an array
--syntax:array.shape
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.shape)

3)reshape:
--The function is used to convert one dimension to another if the elements
are there to convert into the any dimension
syntax:array.reshape(row,col)
eg:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.reshape(2,3))
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr.reshape(3,3))

4)size:
--Is used to find out number of elements present in an array
--syntax:array.size
eg:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.size)

Operations:
--Same as list we can also perform some operations on arrays
1.Indexing
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2[3])

2.slicing
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2[2:5])

3.sum
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.sum())

4.add
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
arr = np.array([7,8,9,10,11,12])
print(arr_2 + arr)
print(arr_2 + 5)

5.sub
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
arr = np.array([7,8,9,10,11,12])
print(arr_2 - arr)
print(arr - 5)

6.mul
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2 * 2)

7.power
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2 ** 3)

8.div
ex:
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2 / 2)

9.max
ex:
import numpy as np
arr_2 = np.array([1,2,3,45,57,100])
print(arr_2.max())

5)arange:
--The arange function is used to generate number in a sequence upto
a limit and it form 1D array
--And this array can convert into 2D arrays by using reshape
syntax: np.arange(range)
ex:
import numpy as np
arr_ = np.arange(1,100)
print(arr_.reshape(3,3))
print(arr_)'''

import numpy as np
arr_ = np.arange(1,10)
arr_2 = arr_.reshape(3,3)
print(arr_2.ndim)
print(arr_)























































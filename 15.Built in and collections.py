'''math:
math module used to work on mathematical functionality

floor:
--it will round down the near value
eg:
import math
print(math.floor(3.78))

Ceil:
eg:
it will round up to near value
import math
print(math.ceil(3.78))

gcd:
it will find the gcd value
eg:
import math
print(math.gcd(24,36))

lcm:It will find the value
eg:
import math
print(math.lcm(24,36))

sqrt:it will get sqrt value
eg:
import math
print(math.sqrt(24))

Factorial:it will give the factorial value
eg:
import math
print(math.factorial(5))

import math
print(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)


random:
--The random module used to get the random number
randint:
used to generate random numbers based on the range
eg:
import random
print(random.randint(1,100))

choice:it will give the random value from the given data
eg:
import random
color = ['red','blue','black']
print(random.choice(color))

shuffle:it can shuffle the data randomly
import random
color = ['red','blue','black']
random.shuffle(color)
print(color)


uniform:Will give the decimal values in a range given
ex:
import random
print(random.uniform(1,100))

sys:
sys module used to get the details of python interpreter

version:the version of python interpreter
eg:
import sys
print(sys.version)

path: .py path we will get by this function
eg:
import sys
print(sys.path)

exit:This function will exit from the program
eg:
import sys
print(sys.exit())

platform:It will gives the python run platform
eg:
import sys
print(sys.platform)

argv:It will give the current file run path
eg:
import sys
print(sys.argv)

datetime:Used to work with date and time
-now:
it will give the today time+ date
from datetime import datetime, date, time
print(datetime.now())

from datetime import datetime
now = datetime.now()
print(now.strftime('%y-%m-%d'))
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%H:%M:%S"))

%y--Will get the year
%m--Will get the month
%d--Will get the day
%H--Will get the hour
%M--Will get the minute
%S--Will get the Second
%A--Will get current day
%B--Will get current month



Collections:
The collections module will provide container type data which is more powerful
than the bulit-in datatypes(dict,list,tuple)
eg:
import collections
data = ['apple','guava','orange','kiwi','guava']
print(collections.Counter(data))

deque:used to work with list
eg:
from collections import deque
how = deque([1,2,3])
how.appendleft(7)
print(how)

extend:
from collections import deque
how = deque([1,2,3])
how.extend([4,5,6])
print(how)

extendleft:
from collections import deque
how = deque([1,2,3])
how.extendleft([4,5,6])
print(how)

pop:
from collections import deque
how = deque([1,2,3])
how.pop()
print(how)

from collections import namedtuple
data = namedtuple("stu",('name','age'))
print(data('sandy','21'))

Itertools:
count:
eg:
from itertools import count
c = count(100)
for j in range(5):
    print(next(c))

repeat:
eg:
import itertools
for j in itertools.repeat('Python',10):
    print(j)

permutations and combinations:
from itertools import permutations, combinations
data = permutations([1,2,3],2)
print(list(data))

any_ = combinations([1,2,3],2)
print(list(any_))
'''

import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())


























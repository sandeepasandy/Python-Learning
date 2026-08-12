'''1)Constructor:
-->__init__
-->The constructor is a special method that only run when the
object is created
-->Mostly we will take data inside this method..
ex:
class cls_data:
    def __init__(self):
        self.name = 'Sandy'
        self.course = 'Python'

cls_ = cls_data()
print(cls_.name)
print(cls_.course)

2)self:
--The self keyword refers to current object
class student:
    def __init__(self):
        self.name = 'Sandy'
    def any_(self):
        print(self.name)

s1 = student()
s1.any_()
ex2:
class student_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age
    def student(self):
        print(f'{self.name} from batch {self.batch} and age is {self.age}')

data1 = student_data('Sandy',5,21)
data1.student()


3)Encapsulation:
--wrapping data and methods together is called encapsulation
and using or controlling the data in methods
Basic ex:
class student_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age
    def student(self):
        print(f'{self.name} from batch {self.batch} and age is {self.age}')

data1 = student_data('Sandy',5,21)
data1.student()

Access specifiers
1.public(name):This can be access normally and can it like a normal variable
syntax:
self.name = name
print(self.name)
ex:
class student_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age
    def student(self):
        print(f'{self.name} from batch {self.batch} and age is {self.age}')

data1 = student_data('Sandy',5,21)
data1.student()

2.protected(_name):Just adding single(_) before a variable it becomes
protected variable
syntax:
self._age = age
print(self._age)
ex:
class student_data:
    def __init__(self,name,batch,age,fee):
        self._name = 'Sandy'
        self._batch = batch
        self._age = age
        self._fee = fee
    def only_name(self):
        print(f"{self._name}")
    def only_batch(self):
        print(f"{self._batch}")
    def only_age(self):
        print(f"{self._age}")
    def only_fee(self):
        print(f"{self._fee}")

data1 = student_data('Sandy',5,21,50000)
data1.only_name()
data1.only_batch()
data1.only_age()
data1.only_fee()

3.private(__name):
adding (__) before a variable it becomes private
syntax:
self.__balance=balance
print(self.__balance)
ex:
class bank_ac:
    def __init__(self):
        self.name = 'sandy'
        self.adr = '234657389389'
        self.pan = 'hd65er2jd5'
        self.__balance = 50000
    def details(self):
        print(self.name)
        print(self.adr)
        print(self.pan)
    def bank_bal(self):
        print(self.__balance)
ac = bank_ac()
ac.details()
ac.bank_bal()

--Example by using public,protected and private specifiers:
class employee:
    def __init__(self):
        self.name = 'Sandy'
        self.role = 'Python programmer'
        self.__salary = 50000
        self._experience = 3
        self._emptype = 'full-time'
    def details(self):
        print(self.name)
        print(self.role)
    def income_(self):
        print(self.__salary)
    def type_(self):
        print(self._experience)
        print(self._emptype)
emp = employee()
emp.details()
emp.income_()
emp.type_()

Practice:'''
class university:
    def __init__(self):
        self.name = 'Sony'
        self.id = 14
        self.city = 'Vizag'
        self.Address = 'NAD kotha Road'
student_ = university()
print(student_.name)
print(student_.id)
print(student_.city)




























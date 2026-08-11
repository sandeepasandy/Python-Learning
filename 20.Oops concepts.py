'''
OOPS
object oriented programming system
OOP is used to maintain the code structure is object and classes
1.class
2.Object
3.Attribute
4.Method

1.Class:
--class is an blueprint or template to an object
class(keyword) Name:
#attribute
#Methods

2.Object:object is the instance of class
syntax:
class(keyword) Name:
#attribute
#methods
any_ = class_name
ex:
class person:
    name = 'sandy'
    Edu = 'B.Tech'
p1 = person()
print(p1.name)
print(p1.Edu)
ex2:
class codegnan:
    City = 'Vizag'
    Tech = 'Python'
    data_ = 'My SQL'
code_ = codegnan()
print(code_.City)

3.Attributes:Attributes is the data present in the class or pass
to the class
Eg:
Take a car attributes are color brand seat
ex1:
class Sandy:
    name = 'Sandeepa'
    age = 21
    Edu = 'B.Tech'
s = Sandy()
print(s.name)
ex2
class car:
    def __init__(self):
        self.color = 'Red'
        self.seat = 4
        self.brand ='BMW'
c1 = car()
print(c1.color)
print(c1.seat)
print(c1.brand)
class sandy:
    def __init__(self):
        self.name = 'Sandeepa'
        self.age = 21
        self.Back_G = 'B.Tech'
s = sandy()
print(s.name)
print(s.age)
print(s.Back_G)
4.Methods:
methods are nothing but the functions that is created inside the clas
class(keyword)name:
    #attributes
    def fun_name(self):
        #code
obj = class_name()
print(obj.fun_name())
ex1:
class student:
    def __init__(self):
        self.name = 'Sandeepa'
        self.age = 21
        self.course = 'Data Analysis'
    def st_name(self):
        print(self.name)
        print(self.age)
        print(self.course)
    def all_data(self):
        print(self.name)
        print(self.age)
stu_ = student()
stu_.st_name()
stu_.all_data()
ex2:
class car:
    def __init__(self):
        self.color = 'blue'
        self.seat = 8
        self.Brand = 'BMW'
    def brake_(self):
        print(f'{self.Brand} brake will apply at speed 250KM')
    def accelater_(self):
        print(f'{self.Brand} will take 2 sec to reach 180 speed')
    def clucth(self):
        print(f'{self.Brand} with {self.seat} is automatic')

Bwm = car()
Bwm.brake_()
Bwm.accelater_()
Bwm.clucth()       

ex3:
class students:
    def __init__(self,name,age,batch):
        self.name = name
        self.age = age
        self.batch = batch
    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.batch)
stu_1 = students('sandy',21,5)
stu_1.all_data()
stu_2 = students('Prudhvi',23,8)
stu_2.all_data()
'''
ex:
class registration_form:
    def __init__(self,name,phonenumber,rollno,branch,Email):
        self.name = name
        self.phonenumber = phonenumber
        self.rollno = rollno
        self.branch = branch
        self.Email = Email
    def details(self):
        print(self.name)
        print(self.phonenumber)
        print(self.rollno)
        print(self.branch)
        print(self.Email)
person = registration_form('Sandeepa',7416829377,3,'CSE','sandeepa.sandy789@gmail.com')
person.details()

































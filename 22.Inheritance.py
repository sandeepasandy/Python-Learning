'''Inheritance
--Inheritance is the process of inherit one class into
another class
--Will  generally inherit from a class is called parent class
and using it in another that class is called child class
ex:
class company:
    def salary(self):
        print('Company salary')
class employee:
    def mon_sal(self):
        print('Employee salary')
per_sal = employee()
per_sal.mon_sal()
per_sal = company()
per_sal.salary()

Types:
1.Single Inheritance:
--If one child class inherit from the one parent class is called single inheritance
ex:
class father:
    def land(self):
        print('5 acer land')
class me(father):
    def flat(self):
        print('6 flat')
all_ = me()
all_.flat()
all_.land()

2.Multiple inheritance:
--If one child inherit from more than one parent class this is called
multiple inheritance
ex:
class father:
    def home(self):
        print('Home at village')
class mother:
    def gold(self):
        print('50kg gold')
class son(father, mother):
    def flat(self):
        print('Sons flat')
all_to = son()
all_to.home()
all_to.gold()
    
3.Multi-level inheritance:
--One child class become parent class to the another class
is called multi-level inheritance
ex:
class grandfather:
    def land(self):
        print('Grandfather land')
class father(grandfather):
    def flat(self):
        print('Father flat')
class son(father):
    def car(self):
        print('Sons car')
fam = son()
fam.land()
fam.flat()
fam.car()

4.Hierarchical inheritance:
--If two child classes inherit from one parent class
is called as hierarchical inheritance
       father
       /   \
      /     \
     /       \
 child1    child2
ex:
class father:
    def land(self):
        print('50 acer land')
class son_1(father):
    def flat(self):
        print('First son flat')
class son_2(father):
    def car(self):
        print('Second Son car')
s1 = son_1()
s1.land()
s1.flat()

s2 = son_2()
s2.land()
s2.car()

5.Hybrid inheritance:
--Inherit from more than two types into one class is called
as hybrid inheritance.
ex:
class person:
    def name(self):
        print('Sandy is her name')
class student(person):
    def study(self):
        print('B.Tech final year')
class py_teacher:
    def teach(self):
        print('Python')
class java_teacher:
    def teac(self):
        print('Java')
class learner(py_teacher,java_teacher):
    def learn(self):
        print('Learner')
class all_get(student,learner):
    def get_it(self):
        print('This person is getting all data ')
an = all_get()
an.name()
an.study()
an.teach()
an.teac()
an.learn()
an.get_it()

class grandfather:
    def land(self):
        print('Grandfather land')
class father(grandfather):
    def flat(self):
        print('Father flat')
class son(father):
    def car(self):
        print('Sons car')
fam = son()
fam.land()
fam.flat()
fam.car()


Practice:
#single inheritance:
class animal():
    def eat(self):
        print('Eating')
class dog(animal):
    def bark(self):
        print('Barking')
an_ = dog()
an_.eat()
an_.bark()

#Multiple Inheritance:
class vehicle():
    def car(self):
        print('This Car is the best')
class vehicle_2():
    def bike(self):
        print('This bike has more features')
class vehicles(vehicle,vehicle_2):
    def auto(self):
        print('Best auto')
all_ = vehicles()
all_.bike()
all_.car()

#Multi-level inheritance:'''
class student:
    def marks(self):
        print('good marks')
class student_2:
    def grade(self):
        print('A')
class student_3(student,student_2):
    def attendance(self):
        print('83%')
all_students = student_3()
all_students.marks()
all_students.grade()
all_students.attendance()


























'''super() method
--This super() method is used to get the constructor from the
parent and use in the child class
--And also can get any method from the class
eg:
class person:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role
        print('Person Constructor called')
class employee(person):
    def __init__(self,name,age,role,salary):
        super().__init__(name,age,role)
        self.salary = salary
        print('Employee Constructor called')
obj = employee('Sandy',21,20000,'Trainee')
print(obj.name)
print(obj.age)
print(obj.role)
print(obj.salary)
ex2:
class all_:
    def job_(self):
        print("I'm looking for a job")
class looking(all_):
    def job_(self):
        super().job_()
        print('We are looking for a candidate')
    def an_(self):
        super().job_()
        print('No jobs')
any_ = looking()
any_.job_()
any_.an_()

Polymorphism:
--Polymorphism means a same name but different forms

1.Method Overloading:
--This method overloading happens in the class a method is created
this same name,but the recent method will be activated and the
before one will not be considered
ex:
class data_:
    def add_(self,a,b,c=0):
        return a+b+c
    def add_(self,a,b,c):
        return a+b+c
    def add_(self,a,b,c,d):
        return a+b+c+d
obj = data_()
print(obj.add_(2,5,7,8))

2.Method Overriding:
--This method overriding happens when a parent class and child class
have same method and the child class takes its own implementation
ex:
class pay:
    def payment(self):
        print('Payment called')
class UPI(pay):
    def payment(self):
        print('UPI payment called')
class Paytm(pay):
    def payment(self):
        print('Paytm payment called')
obj = UPI()
obj.payment()

go = Paytm()
go.payment()

3.Operator Overloading:
--Operator Overloading which gives the special meaning to the
operator when it is called by the object
1.__add__:
class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __add__(self,do):
        print(self.any_ + do.any_)
how = cal(78)
who = cal(67)

print(how + who)

2.__sub__:
class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __sub__(self,do):
        print(self.any_ -  do.any_)
how = cal(78)
who = cal(67)

print(how-who)

3.__mul__:
class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __mul__(self,do):
        print(self.any_ * do.any_)
how = cal(78)
who = cal(67)

print(how*who)

4.__truediv__ #it is for division


'''
class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __truediv__(self,do):
        print(self.any_ / do.any_)
how = cal(78)
who = cal(67)

print(how/who)

















    




































    

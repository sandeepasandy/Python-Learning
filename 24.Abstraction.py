'''Abstraction:
--Abstraction means hiding  the implemented data and showing only need
data to user
--ABC-Abstract base class
--The abstractmethod is used to hide that particular information
of base class
--@abstractmethod is used to know that it is a abstractmethod
from abc import ABC,abstractmethod
class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print('Government interest is 3.5')
class SBI_bank(ABC):
    def interest(self):
        print('SBI bank interest is 7.8')
class ICICI_bank(ABC):
    def interest(self):
        print('ICICI bank interest is 8.9')
obj = SBI_bank()
obj.interest()
obje = ICICI_bank()
obje.interest()

from abc import ABC, abstractmethod

class clg_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print("College fee 45000")
        
class manag(clg_fee):
    def fee_str(self):
        print("College fee 100000")
        
class EM_(clg_fee):
    def fee_str(self):
        print("College fee 15000")
m = manag()
m.fee_str()
e = EM_()
e.fee_str()
create a calculator class which add 2 numbers 3 numbers 4 numbers by using method overriding
create a class with vehicle child classes as bike car bus

class Calculator:
    def add(self,a,b,c=0,d=0):
        return a+b+c+d
cal = Calculator()
print(cal.add(2,5,4))

2.'''
class Vehicle:
    def vehicle_type(self):
        print("This is a vehicle")
class Bike(Vehicle):
    def bike(self):
        print("Bike has 2 wheels")
class Car(Vehicle):
    def car(self):
        print("Car has 4 wheels")
class Bus(Vehicle):
    def bus(self):
        print("Bus is used for transportation")
b = Bike()
b.vehicle_type()
b.bike()
c = Car()
c.vehicle_type()
c.car()
bus = Bus()
bus.vehicle_type()
bus.bus()







































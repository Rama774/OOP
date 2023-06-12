class Grandparents:
    def name(self):
        print('My name is Rama ')


class Parents(Grandparents):
    def family(self):
        print('My family name is Alshareef')


class Child(Parents):
    def age(self):
        print('My age is 15')

rama1=Child()
rama1.name()
rama1.age()
rama1.family()
print('----------------------------------------------------------------------')
class Grandparents:
    def name(self):
        print('My name is Rama ')


class Parents():
    def family(self):
        print('My family name is Alshareef')


class Child(Parents , Grandparents):
    def age(self):
        print('My age is 15')

rama1=Child()
rama1.name()
rama1.age()
rama1.family()
print('----------------------------------------------------------------------')
#polymorphism

print(isinstance(3.5,int))#Bolean

print('----------------------------------------------------------------------')

class A:
    def Rama(self):
        print("This is class A")
class B:
    def Rama(self):
        print("This is class A")

obj1=A()
obj2=B()

name=[obj1,obj2]


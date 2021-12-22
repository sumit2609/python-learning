# <------lec 1------>

# in class we design object

from abc import ABC, abstractmethod


class Computer:
    # method in class
    def config(self):
        print("i5, 16gb, 1tb")


com1 = Computer()
com2 = Computer()
# print(type(com1))

# com1 is parameter to config method in class computer
Computer.config(com1)
Computer.config(com2)

# config will take com1 as parameter
com1.config()
com2.config()

# <------lec 2------>


class Computer:
    # self argument contains com1
    # __init__(self) is a type of constructor
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('ryzen 3', 8)
com1.config()
com2.config()

# <------lec 3------>


class Computer:
    def __init__(self):
        self.name = "sumit"
        self.age = 21

    def update(self):
        self.age = 21

    def compare(self, c2):
        if(self.age == c2.age):
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
# address of c1
# print(id(c1))
c1.update()
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

if c1.compare(c2):
    print("same")
else:
    print("not same")

# <------lec 4------>
# Types of varible


class car:
    # class variables or static variables common variable to all objects of class
    wheels = 4

    def __init__(self):
        # these variable are called instance variable as object changes these variable changes
        self.mil = 10
        self.com = "bmw"


c1 = car()
c2 = car()

c1.mil = 3

car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


# <---------lec 5----------->

# Types of method

# 1. Instance method--> accessor and mutators
# 2. Class method
# 3. static method

class student:

    school = "Panjab university"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    # class methods changes class variable
    # @classmethod is used as decorator
    @classmethod
    def getschoolname(cls):
        print(cls.school)

    # static method---> not dealing with any class or instance variable
    @staticmethod
    def info():
        print("This is student class")


s1 = student(2, 3, 4)
s2 = student(1, 2, 3)

# print(s1.avg())
# s1.set_m1(20)
# print(s1.get_m1())

print(student.getschoolname())
student.info()


# <---------lec 6----------->

# Inner class

class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student('sumit', 105)
s2 = student('tanishk', 106)

# print(s1.name, s1.rollno)
s1.show()

lap1 = s1.lap
lap2 = s2.lap

lap1 = student.laptop()


# <---------lec 7----------->

# Inheritance

# a --> super class/ parent
# b --> sub class/ child
class a:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

# class b is inheriting all feature of class a
# b is child of a


class b(a):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

# multilevel inheritance


class c(b):
    def feature5(self):
        print("feature 5")


a1 = a()
a1.feature1()
a1.feature2()

b1 = b()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()

c1 = c()

# multiple inheritance


class a:
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")


class b:
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


class c(a, b):
    def feature5(self):
        print("feature 5")


c1 = c()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()


# <---------lec 8----------->

#constructor in heritance
# method resolution order----> order is left to right

class a:
    def __init__(self):
        print("in a init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class b(a):
    def __init__(self):
        # with help of this super we call all methods in our parent class
        super().__init__()
        print("in b init")

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


a1 = b()

# ----x-----x------x------x------x


class a:
    def __init__(self):
        print("in a init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")


class b:
    def __init__(self):
        # with help of this super we call all methods in our parent class
        super().__init__()
        print("in b init")

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")


class c(a, b):
    def __init__(self):
        # mro left to right is order
        super().__init__()
        print("in c init")

    def feat(self):
        super().feature2()


a1 = c()
a1.feat()
a1.feature4()


# <---------lec 9----------->
#polymorphism = many-form
# polymorphism is one thing with multiple form

# <---------lec 10----------->
# Duck Typing(way of using polymorphism)

class pycharm:
    def execute(self):
        print("compiling")
        print("Running")


class myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("Running")


class laptop:
    def code(self, ide):
        ide.execute()


ide = myeditor()
lap = laptop()
lap.code(ide)

# <---------lec 11----------->
# operator overloading


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    # we have overload this add method as this __add__ method is for
    # int, str etc but we have made it for student class

    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = student(56, 69)
s2 = student(60, 65)

s3 = s1+s2  # student.__add__(s1,s2)
print(s3.m1)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)

# <---------lec 12----------->
# types of polymorphosim
# method overloading and method overriding

# method overloading:
# lets say wwe have 2 methods with same name but different parameters
# example:
# def avg(a,b)
# def avg(a,b,c)


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0

        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s = a

        return s


s1 = student(58, 69)

print(s1.sum(5))
print(s1.sum(5, 6))
print(s1.sum(5, 6, 7))


# method overriding:
# lets say we have 2 methods with same name and same parameter but are
# in different class

class a:
    def show(self):
        print("in A show")


class b(a):
    def show(self):
        print("in B show")


a1 = b()
a1.show()

# <---------lec 12----------->
# abstract class and method in python

# abstract class:
# class containing abstract method is callled abstract class
# can't create object of abstract class

# abstract method:
# method which have only declaration but not defination is called abstract method

# use of abstract class
#


class computer(ABC):
    @abstractmethod
    def process(self):
        pass


class laptop(computer):
    def process(self):
        print("it's running")


class whiteBoard(computer):
    def write(self):
        print("it's writing")


class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com.process()


# can't do this
# com = computer()
# com.process()

com1 = laptop()
com1.process()
com2 = whiteBoard()
prog1 = Programmer()
prog1.work(com2)

#1.Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.

# class String():
#     def __init__(self):
#         self.s = ""
#
#     def get_string(self):
#         self.s = input("Enter a string:")
#     def print_string(self):
#         print(self.s.upper())
#
# obj=String()
# obj.get_string()
# obj.print_string()

#2.Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.
# def putNumber(n):
#     i=0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
# for i in putNumber(100):
#     print(i)

#3.Define a class named American which has a static method called printNationality
# class American(object):
#     @staticmethod
#     def printNationality():
#         print("America")
#
# anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()

#4.Define a class, which have a class parameter and have a same instance parameter

class Person:
    name="Person"
    def __init__(self,name=None):
        self.name=name
jeffrey=Person(" jeffrey")
print("%s name is %s" %(Person.name,jeffrey.name))
nico=Person()
nico.name="Nico"
print("%s name is %s" % (Person.name, nico.name))














#5.. Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.


# class Circle(object):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return self.radius**2*3.14
# aCircle=Circle(2)
# print(aCircle.area())

#6.Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
# class Rectangle(object):
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#     def area(self):
#         return self.length*self.breadth
# aRectangle=Rectangle(2,10)
# print(aRectangle.area())

#7.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# class Shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,l):
#         Shape.__init__(self)
#         self.length=l
#     def area(self):
#         return self.length*self.length
# aSquare=Square(3)
# print(aSquare.area())

#8.Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class
# class Person(object):
#     def getGender(self):
#         return "Unknown"
# class Male(Person):
#     def getGender(self):
#         return "Male"
# class Female(Person):
#     def getGender(self):
#         return "Female"
# aMale=Male()
# aFemale=Female()
# print(aMale.getGender())
# print(aFemale.getGender())
#9. Define a class named American and its subclass NewYorker.
#Hints:Use class Subclass(ParentClass) to define a subclass.
# class American:
#     pass
# class Newyorker(American):
#     print("I'am from Newyork")
# A=American()
# N=Newyorker()













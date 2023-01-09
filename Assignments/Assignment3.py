"""1.Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped."""
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def Perimeter(self):
#         return 2 * (self.length + self.width)
#     def Area(self):
#         return self.length * self.width
#     def display(self):
#         print("The length of rectangle is: ", self.length)
#         print("The width of rectangle is: ", self.width)
#         print("The perimeter of rectangle is: ", self.Perimeter())
#         print("The area of rectangle is: ", self.Area())
# class Parallelepipede(Rectangle):
#     def __init__(self, length, width, height):
#         Rectangle.__init__(self, length, width)
#         self.height = height
#     def volume(self):
#         return self.length * self.width * self.height
# A = Rectangle(7, 5)
# A.display()
# B = Parallelepipede(7, 5, 2)
# print("the volume of myParallelepipede is: ", B.volume())

"""2.Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# # Create a student object via an instantiation on the Student class and then test the displayStudent method."""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Person name : ", self.name)
#         print("Person age = ", self.age)
# class Student(Person):
#     def __init__(self, name , age , section):
#         Person.__init__(self,name, age)
#         self.section = section
#     def displayStudent(self):
#         print("Student name : ", self.name)
#         print("Student age = ", self.age)
#         print("Student section = ", self.section)
# P = Person("Anjaly", 28)
# P.display()
# S = Student("Anju", 23 , "Mathematics")
# S.displayStudent()

"""3.Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:"""
class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
    def perimeter(self):
        return 2 * 3.14 * self.r

    def area(self):
        return 3.14 * self.r ** 2
    def test_belong(self, x, y,a,b):
        self.x=x
        self.y=y
        dist=(self.x-self.a)*(self.x-self.a)+(self.y-self.b)*(self.y-self.b)
        if dist<=self.r**2:
            print("point is inside the circle C")
        else:
            print("point is outside the circle C")
C = Circle(1, 2, 1)
print("the perimeter of the circle C is:", C.perimeter())
print("the area of circle C is:", C.area())
C.test_belong(4,4,1, 1)

"""4. Define a Book class with the following attributes: Title, Author (Full name), Price.
Define a constructor used to initialize the attributes of the method with values entered by the user.
Set the View() method to display information for the current book.
Write a program to testing the Book class."""
# class Book:
#     def __init__(self, Title, Author, Price):
#         self.Title = Title
#         self.Author = Author
#         self.Price = Price
#     def view(self):
#         return ("Book Title: ", self.Title, "Book Author: ", self.Author, "Book Price: ", self.Price)
# MyBook = Book("Harry Potter & the Chamber of Secrets", "J K  Rowling", "630")
# print(MyBook.view())
"""5.Coding a class named myString inheriting from the str class allowing to endow strings with append() and pop () methods doing the same operations as those of lists class."""
# class str:
#     list=[5,6,7,8,9,10]
# class mystring(str):
#     def append(self,new):
#         self.list.append(new)
#         print(self.list)
#     def pop(self,item):
#         self.list.pop(item)
#         print(self.list)
# A=mystring()
# A.append(6)
# A.pop(2)













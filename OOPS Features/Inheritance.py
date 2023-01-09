"""
Inheritance:Child class inherit the properties of parent class
"""
#Parent class
# class Person:
#     def __init__(self,name,contact):
#         self.name=name
#         self.contact=contact
#     def address(self):
#         print(self.name,self.contact)
#
# #child class
# class Doctor(Person):
#     def sample(self):
#         print("Test msg")
# class Patient(Person):
#     pass
# A=Doctor.sample('gfjgkjl')
# doc=Person("Anu",1234567)
# pat=Person("Anju",987654321)
# doc.address()
# pat.address()






# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def getData(self):
#         self.name=input("Enter your name=")
#         self.mark=input("Enter your mark=")
#     def putData(self):
#         print(self.name,"\n",self.mark)
# obj=student(' ',' ')
# obj.getData()
# obj.putData()
"""Single Inheritance"""
# class student:
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         self.name=input("Enter your name=")
# class hod(student):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def putData(self):
#         self.hodname=input("Enter your hodname=")
#     def display(self):
#         print("student name is ",self.name)
#         print("HOD name is ", self.hodname)
# obj=hod(' ')
# obj.getData()
# obj.putData()
# obj.display()
"""Multiple Inheritance"""
# class A:
#     def __init__(self,name):
#         self.name=name
#     def getData(self):
#         self.name=input("Enter your name=")
# class B(A):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def putData(self):
#         self.hodname=input("Enter your hodname=")
# class C(B):
#     def fun3(self):
#         print("This is class C")
# class D(C):
#     def fun4(self):
#         print("This is class D")
#
#     def display(self):
#         print("student name is ",self.name)
#         print("HOD name is ", self.hodname)
# obj=D(' ')
# obj.getData()
# obj.putData()
# obj.fun3()
# obj.fun4()
# obj.display()

"""1.Multilevel Inheritance"""
# class A:
#     def get1(self):
#         print("I am A class")
# class B:
#     def get2(self):
#         print("I am B class")
# class C(A,B):
#     def putData(self):
#         print("yes  am inherited A & B")
# obj=C()
# obj.get1()
# obj.get2()
# obj.putData()
"""2.Multilevel Inheritance"""
# class employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
# class childemployee1(employee):
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
# class childemployee2(employee):
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
# A=employee('Anu',24,25000)
# A.childemployee1()


# class Grandfather:
#     def ownHouse(self):
#         print("Grandpa House")
# class Father(Grandfather):
#     def OwnBike(self):
#         print("Father's Bike")
# class Son(Father):
#     def ownBook(self):
#         print("son have a book")
# A=Son()
# A.ownHouse()
# A.OwnBike()
# A.ownBook()


# class Person:
#     def speak(self):
#         print('I can speak')
# class Man(Person):
#     def wear(self):
#         print("I wear shirt")
# class Woman(Person):
#     def wear(self):
#         print("I wear skirt")
# man=Woman()
# man.wear()
# man.speak()

# class Emp:
#     def empdetails(self):
#         print("Employee details")
# class Emp1:
#     def test(self):
#         print("Name")
# class Emp2(Emp,Emp1):
#     def emp2(self):
#         print("Age")
# obj=Emp2()
# obj.test()
# obj.empdetails()
# obj.emp2()


class cal1:
    def sum(self,a,b):
        return a+b
class cal2:
    def sub(self,a,b):
        return a-b
class cal3(cal1,cal2):
    def div(self,a,b):
        return a/b
A=cal3()
print(A.sub(10,2))
print(A.sum(10,2))
print(A.div(10,2))



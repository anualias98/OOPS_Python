"""Encapsulation is wrappig up of data"""

# #Protected Access Modifier
# #super class
# class Student:
#     #protected data members
#     _name=None
#     _roll=None
#     _banch=None
#     #constructor
#     def __init__(self,name,roll,branch):
#         self._name=name
#         self._roll=roll
#         self._branch=branch
#         #protected member function
#     def _displayRollAndBranch(self):
#         #accessing protected data members
#         print("Roll:",self._roll)
#         print("Branch:",self._branch)
#         #derived class
# class Myclass(Student):
#     #constructor
#     def __init__(self,name,roll,branch):
#         Student.__init__(self,name,roll,branch)
#     def displayDetails(self):
#         #accessing protected data members of superclass
#         print("Name:",self._name)
#         #accessing protected data member function of superclass
#         self._displayRollAndBranch()
#         #creating objects of the derived class
# obj=Myclass("Anu",123456,"Python Fullstack")
# #calling public member functions of the class
# obj.displayDetails()
#private access modifier
class Myclass:
    __name=None
    __roll=None
    __branch=None
    def __init__(self,name,roll,branch):
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    def __displayDetails(self):
        print("Name:",self.__name)
        print("Roll:",self.__roll)
        print("Branch:",self.__branch)
    def accessPrivateFunction(self):
        self.__displayDetails()
obj=Myclass("Anju",123456,"Python Django")
obj.accessPrivateFunction()




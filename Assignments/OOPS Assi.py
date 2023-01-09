#1.Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.
# seating_capacity() a default value of 50.
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     # assign default value to capacity
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# bus = Bus("Bus", 140, 12)
# print(bus.seating_capacity(50))


#2.Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance,
# we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage= mileage
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self,capacity):
        fare=capacity*100
        return fare
class Bus(Vehicle):
    def amount(self):
        t1 = Vehicle.fare(self,50)
        total= t1+(10*t1) / 100
        print("Total amount is ",total)
bus = Bus("Bus", 100, 50)
bus.amount()



class StringManipulator:
    def __init__(self):
        self.text = ""

    def get_text(self):
        self.text = input("Enter a string: ")

    def print_text_uppercase(self):
        print(self.text.upper())

manipulator = StringManipulator()
manipulator.get_text()
manipulator.print_text_uppercase()

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

square = Square(5)
print("Area of square:", square.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 6)
print("Area of rectangle:", rectangle.area())

import math

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def show_coordinates(self):
        print("Coordinates:", self.x_coordinate, ",", self.y_coordinate)

    def move_coordinates(self, dx, dy):
        self.x_coordinate += dx
        self.y_coordinate += dy

    def distance_to_point(self, other_point):
        return math.sqrt((self.x_coordinate - other_point.x_coordinate)**2 + (self.y_coordinate - other_point.y_coordinate)**2)

point1 = Point(1, 2)
point2 = Point(4, 6)
point1.show_coordinates()
point2.show_coordinates()
print("Distance between points:", point1.distance_to_point(point2))

class Account:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

acc = Account("Almas", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1500)

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1, numbers))
print("Prime numbers:", prime_numbers)

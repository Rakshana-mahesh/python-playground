# 1. Create a simple class with attributes and methods
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        else:
            return "C"

s1 = Student("Sakura", 92)
print(s1.name, "got grade:", s1.get_grade())

# 2. Class with a method that updates its own data
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount

acc = BankAccount("Sakura", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.balance)

# 3. Class inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

d = Dog("Rex")
print(d.speak())

# 4. Class with a list attribute (like a to-do list)
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        return self.tasks

todo = TodoList()
todo.add_task("Practice Python")
todo.add_task("Push to GitHub")
print("Tasks:", todo.show_tasks())

# 5. Class representing a simple Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
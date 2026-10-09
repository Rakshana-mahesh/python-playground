# 1. Function with *args - sum any number of arguments
def add_all(*args):
    return sum(args)

print("Sum of 1,2,3:", add_all(1, 2, 3))
print("Sum of 5,10,15,20:", add_all(5, 10, 15, 20))

# 2. Function with **kwargs - print student details
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Rakshana", age=20, course="CSD")

# 3. Lambda function - square a number
square = lambda x: x ** 2
print("Square of 6:", square(6))

# 4. Using lambda with sorted() - sort list of tuples by second value
students = [("Sakura", 85), ("Rex", 92), ("Milo", 78)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Sorted by marks:", sorted_students)

# 5. Using map() and filter() with lambda
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled = list(map(lambda x: x * 2, nums))
even_only = list(filter(lambda x: x % 2 == 0, nums))
print("Doubled:", doubled)
print("Even only:", even_only)
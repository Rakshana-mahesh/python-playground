#Write to a file and read it back
def write_and_read(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    with open(filename, "r") as f:
        return f.read()

result = write_and_read("notes.txt", "Learning Python is fun")
print("File content:",result)

#Count numbers of lines in a file
def count_lines(filename):
    with open (filename, "r") as f:
        lines = f.readlines()
    return len(lines)
with open ("sample.txt", "w") as f:
    f.write("Line one\nLine Two\nLine Three\n")
print("Number of lines:", count_lines("sample.txt"))

#Handle zero by deivision safely
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("Error: Division by zero is not allowed.")
print("10/2=", safe_divide(10, 2))
print("10/0=", safe_divide(10, 0))

#Handle invalid input safely
def safe_int_convert(value):
    try:
        return int(value)
    except ValueError:
        return("Invalid input. Please enter a valid integer.")
print(safe_int_convert("123"))
print(safe_int_convert("abc"))

#Append text to  an existing file

def append_to_file(filename, text):
    with open (filename, "a") as f:
        f.write(text + "\n")
        append_to_file("notes.txt", "Day 5 of Learning Python!")
    with open ("notes.txt", "r") as f:
        print("Updated content.txt:", f.read())
    
    

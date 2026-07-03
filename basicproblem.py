#Sum of two numbers
a = 7
b = 3
print("Sum :" ,a+b)

#Check even or odd
num = 7
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

#Find the largest of three numbers
x,y,z = 10,40,70
largest = max(x,y,z)
print("Largest :", largest)

#Reverse String
text = "Nithesh"
print("Reversed:",text[::-1])

#Factorial using Loop
n=5
fact=1
for i in range(1, n+1):
    fact *=i
print("Factorial of" ,n, "is" ,fact)
#print multiplication table of 1 to 10
num = 7
for i in range(1,11):
    print(num,"x",i, "=" ,num*i)

#sum of digits of a number
n = 2122
total = 0
while n>0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)

#check if a number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
         return False
    return True
print("Is 17 prime?",is_prime(17))

# print fibonacci series upto n terms
n_terms = 10
a ,b = 0 , 1
fib_series =[]
for _ in range(n_terms):
    fib_series.append(a)
    a,b = b , a+b
    print("Fibonacci series:", fib_series)

#Count vowels in a string
text = "Rakshana loves python"
vowels = "aeiouAEIOu"
count = sum(1 for char in text if char in vowels)
print("Vowel count:",count)



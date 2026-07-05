#Functions to  check palindrome

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
print("Is 'level' a palindrome?",is_palindrome("Level"))

#WFunctions to count words in a sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = "I am learning python programming"
print("Words count:",count_words(sentence))

#Functions to find average of a list

def find_average(numbers):
    return sum(numbers)/len(numbers)
marks =[85, 90, 78, 92, 88]
print("Average marks:",find_average(marks))

#Functions to swap 2 variables

def swap(a,b):
    return b,a
a,b = 7,10
a,b = swap(a,b)
print("After swapping: x =", a,"y =",b)

#Functions to check if the string contains only digits

def is_numberic(s):
    return s.isdigit()
print("Is '12345' numeric?", is_numberic("12345"))
print("Is 'ab123' numeric?", is_numberic("ab123"))

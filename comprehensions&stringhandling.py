# 1. List comprehension - squares of numbers
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

# 2. List comprehension with condition - even numbers only
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Evens:", evens)

# 3. Dictionary comprehension - word lengths
words = ["python", "code", "github", "practice"]
word_lengths = {word: len(word) for word in words}
print("Word lengths:", word_lengths)

# 4. String formatting with f-strings
name = "Rakshana"
day = 7
print(f"Hey {name}, you're on Day {day} of your Python journey!")

# 5. Check if a string is an anagram of another
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))
print("Are 'hello' and 'world' anagrams?", is_anagram("hello", "world"))
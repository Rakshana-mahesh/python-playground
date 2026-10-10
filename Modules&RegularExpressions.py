import re
import random
import datetime

# 1. Using the random module - simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

print("Dice roll:", roll_dice())

# 2. Using the datetime module - get current date and day
today = datetime.date.today()
print("Today's date:", today)
print("Day of week:", today.strftime("%A"))

# 3. Regex - validate an email address
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print("Valid email?", is_valid_email("rakshana@gmail.com"))
print("Valid email?", is_valid_email("not-an-email"))

# 4. Regex - extract all numbers from a string
text = "I have 2 cats, 5 fish, and 10 books"
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

# 5. Regex - replace all spaces with underscores
sentence = "Rakshana is learning Python"
underscored = re.sub(r"\s+", "_", sentence)
print("Underscored:", underscored)
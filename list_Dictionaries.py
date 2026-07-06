#Find the second largest number in the list

def second_largest(numbers):
    unique_nums = list(set(numbers))
    unique_nums.sort()
    return unique_nums[-2]

marks = [10, 20, 4, 45, 99, 99, 45]
print("Second largest number is:", second_largest(marks))

#Remove duplicates from the list
def remove_duplicates(lst):
    return list(set(lst))
nums = [1, 2, 2, 3, 4, 4, 5]
print("List after removing duplicates:", remove_duplicates(nums))

#Count occuurences of each element in the list
def count_occurrences(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']
print("Occurrences of each fruit:", count_occurrences(fruits))

#Merge two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
person = {"name: Sakura", "age:20"}
extra_info = {"City": "Coimbatore", "Course":"CSD"}
print("Merged:",merge_dicts(person, extra_info))

#Find the most frequent element in the list
def most_frequent(lst):
    counts = count_occurrences(lst)
    return max(counts, key=counts.get)
print("Most frequent fruit is:", most_frequent(fruits))
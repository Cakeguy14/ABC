#todo list comprehension - a concise way to create lists in python
# compact and easier to read than traditional loops
# [expression for value in iterable if condition]

# triples = [x * 3 for x in range(10)]
# squares = [y * 2 for y in range(10)]
# print(squares)
# print(triples)

# fruits = ["apple", "banana", "orange", "grape"]
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)
# print(fruits)


numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
positive_num = [num for num in numbers if num > 0] #todo num for num in numbers if num >=0...  num for num in numbers searches for if num >=0 and returns only num which is positive
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 != 0] #todo odd_num = [num for num in numbers if num % 2 == 1]

print(odd_num)
print(even_num)
print(positive_num)
print(numbers)
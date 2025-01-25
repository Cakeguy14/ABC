# this is my first python program
# print("Hello World")
# print("Im your new king")
#
#
#
# Greatness = "kumaran"
# goat = "you are peak"
# print(f"hello {Greatness}")
# print(f"goat {goat}")
# price = 12.44
#
#
# print(f"per cake ${price}")
#
# is_good = True
#
# if is_good:
#     print(f"ok to eat")
# else:
#     print(f"dont eat")
#
# num = 123
# name = "kumaran"
# decimal = 12.23
# good = True
# age = 25
#
# print(type(decimal))
#
# num = int(num)
# num = int(num)
#
# #TODO: Reinilization
#
# name = float(num)
# name += 1
# print(name)
#
# name = input("Name?: ")
# age = int(input("Age?: "))
# age += 1
# print (f"hello {name}!")
# print (f"you are {age}")
#
# item = input("Name of the item: ")
# quantity = int(input("no of item: "))
# price = float(input("price of item: "))
# total = price * quantity
# print(total)
# print(f"you have bought {quantity} x {item}/s")
# print(f"for ${total}")
#
# #todo wrod game
#
# A = input("enter an object: ")
# B = input("enter a verb: ")
# C = input("enter a verb: ")
# D = input("enter a noun: ")
#
# print(f"Life sometimes throws {A} at your door step")
# print(f"if you {B} that dont {C} it")
# print(f"it all was in the {D}")
#
# #todo math
#
# import math
# radius = float(input("Enter radius: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is: {circumference}")
#
# R = float(input("Enter Radius: "))
# A = math.pi * pow(R,2)
# print(f"{round(A, 2)}")
#
# c=a²+b²
#
# A = float(input("enter A: "))
# B = float(input("enter b: "))
# C = math.sqrt(pow(A, 2)+pow(B, 2))
# print(C)
#
# #todo if else
#
# Response = input("Enter yes or no: ")
#
# if Response == yes:
#     print("you got it sir")
# else:
#     print("ok thanks for answering")
#
# name = input("Enter your name: ")
#
# if name == "":
#     print("you did not enter your name")
# else:
#     print(f"hello {name}")
#
# item = input("Enter an item: ")
# for_sale = True
# coconut = 40
# mango = 100
# orange = 150
# for_sales = [coconut, mango, orange]
# if for_sale >= 100:
#          print(f"The item is {for_sales} available for long time")
# elif for_sale <= 50:
#     print(f"The item is {for_sales} only for short time")
# if for_sale == False:
#     print(f"The item is {for_sales} not for sale")
#
# #todo python calculator - using arithmetic functions
#
# symbol = input("Enter a symbol(+ / * -): ")
# num1 = float(input("Enter any number: "))
# num2 = float(input("Enter any number: "))
#
# num1 = float(num1)
# num2 = float(num2)
#
# if symbol == "+":
#     result = num1 + num2
#     print(result)
# elif symbol == "-":
#     result = num1 - num2
#     print(result)
# elif symbol == "/":
#     result = num1 / num2
#     print(result)
# elif symbol == "*":
#     result = num1 * num2
#     print(result)
# else:
#     print(f"{symbol}correct ila olunga podra dei")
#
# #TODO:weight converter using if else
#
#
# weight = float(input("Enter weight in (kg/lb): "))
# measure = input("Enter metric (kg/lb): ")
# kg = weight
# lb = (2 * weight)
# if measure == kg:
#     print(f"Your weight is {kg} kg")
# else:
#     print(lb)
#
# weight = float(input("Enter weight in (kg/lb): "))
# unit = input("Enter unit (kg/lb): ")
#
# if unit == "kg":
#     weight = weight * 2.20462
#     print(f"Your weight is {weight} lb")
# elif unit == "lb":
#     weight = weight / 2.20462
#     print(f"Your weight is {weight} kg")
# else:
#     print("Enter a valid unit")
#
# #todo if else
#
# unit = input("Enter unit (F/C): ")
# num = float(input("Enter temperature: "))
#
# if unit == "F":
#     unit = round((num - 32) * 5/9, 1)
#     num = "C"
#     print(f"your temperature is {unit}{num}")
# elif unit == "C":
#     unit = round((num * 9/5) + 32, 1)
#     num = "F"
#     print(f"your temperature is {unit}{num}")
# else:
#     print("Enter a valid unit")
#
# # #TODO not-inverts boolean , OR-at least one condition should be True, AND- both the condition should be True
#
# bridge = int(input("Enter the length of the bridge: "))
# broken = bool(input("Is the bridge broken? (True/False): "))
#
#
# if bridge < 100 and broken == True:
#     print("bridge is broken")
# else:
#     print("bridge is not broken")
#
#
# # #todo if else - terenary
#
# age = 25
#
# print("you are a" + ("child" if age < 18 else "n adult"))
#
# #todo #todo String methods-Functions
#
#
# name = "kumaran"
# result = name.upper()
# print(result)
#
#
# name = "kumaran"
# result = name.lower()
# print(result)
#
#
# name = "kumaran"
# result = name.isdigit()
# print(result)
# name = "kumaran"
# result = len(name)
# print(result)
#
# name = "kumaran"
# result = name.find("n")
# print(result)
#
# name = "kumaran"
# result = name.rfind("q")
# print(result)
#
# name = "kumaran"
# result = name.capitalize()
# print(result)
#
# name = "kumaran"
# result = name.isalpha()
# print(result)
#
# name = "kumaran"
# result = name.count("a")
# print(result)
#
# name = "kumaran"
# result = name.replace("k", "K")
# print(result)
#
# print(help(str))
#
# name = input("Enter your name: ")
#
# result = name.isalpha(), len(name) <= 12
# print(result)
#
# name = input("Enter your name: ")
#
# if name.isalpha():
#     print("your name is valid")
# elif len(name) <= 12:
#     print("your name is valid")
# else:
#     print("your name is invalid")
#     print(name)
#
# #todo Indexing
#
# name = "kumaran"
#
# print(name[0])
# print(name[0:6])
# print(name[:7])
# print(name[5:])
# print(name[-4])
# print(name[::3])
# print(name[::-1])
# result = name[-4:]
# print(f"your name is {result}")
#
# #todo Format specifiers
# num = 1234516.123
#
# print(f"your number is ${num:.1f}")
# print(f"your number is ${num:10}")
# print(f"your number is ${num:010}")
# print(f"your number is ${num:>10}")
# print(f"your number is ${num:<10}")
# print(f"your number is ${num:^10}")
# print(f"your number is ${num:+}")
# print(f"your number is ${num: }")
# print(f"your number is ${num:,}")
#
# #todo while loop
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# while name == "":
#     print("you did not enter your name")
#     name = input("Enter your name: ")
# print(f"hello {name}")
#
# while age < 18:
#     print("you did not enter your name")
#     name = input("Enter your age: ")
# print(f"hello you are {age}years old")
#
# num = int(input("Enter a number between 1 and 10: "))
#
# while num < 1 or num > 10:
#     print("you have entered the wrong number")
#     num = int(input("Enter a number between 1 and 10: "))
# print(f"your number is {num}")
#
#
# P = float(input("Enter principle: "))
# R = float(input("Enter rate: "))
# T = int(input("Enter time: "))
# N = 100
#
# while P < 0:
#     print("you have entered the wrong number")
#     P = float(input("Enter principle: "))
#
#     while R < 0:
#         print("you have entered the wrong number")
#         R = float(input("Enter rate: "))
#
#         while T < 0:
#             print("you have entered the wrong number")
#             T = int(input("Enter time: "))
# Formula = P * (pow((1 + R/N), T))
# print(f"your final amount is ${Formula}")
#
# #todo while with break
# while True:
#     P = float(input("Enter principle: "))
#     if P < 0:
#         print("you have entered the wrong number")
#     else:
#         break
#
# while True:
#     R = float(input("Enter rate: "))
#     if R < 0:
#         print("you have entered the wrong number")
#     else:
#         break
#
# while True:
#     T = int(input("Enter time: "))
#     if T < 0:
#         print("you have entered the wrong number")
#     else:
#         break
# Formula = P * (pow((1 + R/N), T))
# print(f"your final amount is ${Formula}")
#
# #todo for loop
# x = 1234567890
# for x in range(1, 11):
#     print(x)
#
# for x in reversed(range(1, 11)):
#     print(x)
#
# for x in range(1, 11, 2):
#     print(x)
#
# for x in range(1, 11):
#     if x == 5:
#         continue
#     else:
#         print(x)
#
# for x in range(1, 11):
#     if x == 5:
#         break
#     else:
#         print(x)
#
# #todo import time
#
# import time
#
# x = int(input("Enter time: "))
#
# for x in range(x, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("hello")
#
# #todo clock timer
# for x in range(x, 0, -1):
#     seconds = x % 60
#     minutes = int(x // 60)
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print(x, end="")
#
# #todo horizontal
# row = int(input("Enter time: "))
# column = int(input("Enter time: "))
# symbol = input("Enter symbol: ")
# for x in range(row):
#     for y in range(column):
#         print(symbol, end="")
#     print()
#
#
# #todo collections

#todo List'

# x = [1, 2, "3", 4, 5]
# print(x[1:3])
# print(x[:3])
# print(x[::3])
# print(x[::-1])
# print(dir(x))
# print(help(x))
# print(x.index(3))
# print(x.count(3))
# x.append(6)
# x.remove(2)
# print(x)
# print(len(x))
# print(2 in x)
# print("3" in x)
#
#
# x[0] = 2
# y = x.pop(0)
# for y in x:
#     print(y)
#
# x[0] = 2
# for y in x:
#     print(y)
from operator import index
from tabnanny import process_tokens
from urllib.response import addbase

# x = [1, 2, 3, 4, 5]

# x.remove(2)
# x.append(89)
# x.insert(0, 7)
# x[0] = 2 #todo replacing function
# x.sort()
# x.reverse()
# # x.clear()
# # print(index(2 in x))
# print(x.index(2))
# # print(index(x.count(3) == 1))
#
# print(x)

# for x in range(1, 11, 2):
#     print(x)
#
# for x in range(1, 11):
#     if x == 5:
#         continue
#     else:
#         print(x)
#
# for x in range(1, 11):
#     if x == 5:
#         break
#     else:
#         print(x)

#todo set={}  unordered and immutable, No duplicates, but add/removed is ok

# fruits = {"apple", "banana", "cherry"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print(fruits[0]) #todo index func will not work in set as it is unordered

# fruits = {"apple", "banana", "cherry"}
# # fruits.add("orange")
# # fruits.remove("apple")
# # fruits.discard("cherry")
# # fruits.pop() #todo removes the first element but not ordered
# # fruits.clear()
# print(fruits)

#todo tuple=() ordered unchangeable, duplicates are ok, faster

# fruits = ("apple", "banana", "cherry")

# print(fruits[0])
# print(fruits[1])
# print(len(fruits))
# print(dir(fruits))
# print("pineapple" in fruits)
# print(fruits.index("cherry"))
# print(fruits.count("cherry"))
# print(fruits)

#todo shopping cart program using collections-list
#
# Items = []
# Prices = []
# total = 0
#
# while True: #todo if the condition of while is True we need a break to break out of it at some point
#     Item = input("enter item name(q to quit): ")
#     if Item.lower() == "q":
#         break
#     else:
#         Price = float(input(f"enter item price ({Item}): ")) #todo "enter item price" {Item}:
#         Items.append(Item)
#         Prices.append(Price)
# print("/////////////////your cart is//////////////////")
# for Item in Items:
#     print(Item, end= " ")
# for Price in Prices:
#     total += Price
# print()
# print(f"total is {total}")


# Items =     ["Fruits", "Vegetables", "Bread", "Meat"]
# Beverages = ["Sugar", "Milk", "Milkshake", "Coffee"]
# Utensils  = ["Kettle", "Spatula", "Plate", "Fork"]

# cart = [Items, Beverages, Utensils]

# cart = (["Fruits", "Vegetables", "Bread", "Meat"],
#         ["Sugar", "Milk", "Milkshake", "Coffee"],
#         ["Kettle", "Spatula", "Plate", "Fork"])

# cart = (("Fruits", "Vegetables", "Bread", "Meat"),
#         ("Sugar", "Milk", "Milkshake", "Coffee"),
#         ("Kettle", "Spatula", "Plate", "Fork"))

cart = ({"Fruits", "Vegetables", "Bread", "Meat"},
        {"Sugar", "Milk", "Milkshake", "Coffee"},  #todo have to check this once
        {"Kettle", "Spatula", "Plate", "Fork"})

# cart.append(["Oil", "Water"])
# print(cart[0][3], end=" ") #todo since the columns are in place we can use end=" " to make it a row
# print(cart[1][1], end=" ")
# print(cart[2][2], end=" ")
# print(cart[0][3]) #todo since the columns are in place we dont need to use end=" " to make it a row
# print(cart[1][1])
# print(cart[2][2])  #todo Remember - end=" " can be given inside print statements

# print(cart)
# for x in num_pad:
#     for y in x:
#         print(y, end=" ")
#     print(y) #todo why we give final print outside the loop - then only new line by line rows will be shown

# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*",0 ,"#"))
#
# for x in num_pad:
#     for y in x:
#         print(y, end=" ")
#     print() #todo just give print() to print whatever there is - if we give print(y) it'll give duplicates


# Questions = ("what is name of france tower?: ", #todo 0
#              "what is name of old japan?: ",    #todo 1
#              "what is name of biggest animal?: ") #todo 2
#
# options = (("A.Paris", "B.Tokyo", "C.Lion"),
#            ("A.Osaka", "B.Japan", "C.Tiger"),
#            ("A.Elephant", "B.Bird", "C.Monkey"))
#
# Answers = ("A", "A", "A")
# Score = 0
# Question_num = 0
# Guesses = []
#
#
# for Question in Questions:
#     print("--------------------------")
#     print(Question)
#     for option in options[Question_num]:
#         print(option)     #todo += moves to next and upcoming indexes
#     Guess = input("Enter your answer: ")
#     Guesses.append(Guess)
#     if Guess == Answers[Question_num]:
#         Score += 1
#         Question_num += 1
#         print("Correct")
#     else:
#         print("Wrong")
#
# print("Answers: ",end=" ")
# for answer in Answers:       #todo to get out of the quotation or string and change to index
#     print(answer, end=" ")
# print()    #todo new line
#
# print("Guesses: ",end=" ")
# for guess in Guesses:
#     print(guess, end=" ")
# print()
#
#
# score = int(Score / len(Questions) * 100)
# print(f"Your score is {score} %")



# for Question in Questions:
#     print("--------------------------")
#     print(Question)
#     for option in options[Question_num]:
#         print(option)
#     Question_num += 1  #todo += moves to next and upcoming indexes
#     answer = input("Enter your answer: ")
#     if answer == Answers[Question_num - 1]:
#         print("Correct")
#     else:
#         print("Wrong")


# for x in Question:
#     print(Question_num + 1, x)
#     Question_num += 1






# Question_index = 0
# while Question_index < len(Question):
#     print(Question[Question_index])
#     for x in range(3):
#         print(option[Question_index][x], Answer[Question_index][x])
#     answer = input("Enter your answer: ")
#     if answer == Answer[Question_index][0]:
#         print("Correct")
#     else:
#         print("Wrong")
























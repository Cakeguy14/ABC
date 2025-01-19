"""this is my first python program
print("Hello World")
print("Im your new king")
"""
import math
from operator import truediv
from xmlrpc.server import MultiPathXMLRPCServer

#Greatness = "kumaran"
#goat = "you are peak"
#print(f"hello {Greatness}")
#print(f"goat {goat}")
#price = 12.44

#
# print(f"per cake ${price}")
#
# is_good = True
#
# if is_good:
#     print(f"ok to eat")
# else:
#     print(f"dont eat")

# num = 123
# name = "kumaran"
# decimal = 12.23
# good = True
# age = 25

# print(type(decimal))

# num = int(num)
# num = int(num)

#TODO: Reinilization

# name = float(num)
# name += 1
# print(name)

# name = input("Name?: ")
# age = int(input("Age?: "))
# age += 1
# print (f"hello {name}!")
# print (f"you are {age}")

# item = input("Name of the item: ")
# quantity = int(input("no of item: "))
# price = float(input("price of item: "))
# total = price * quantity
# print(total)
# print(f"you have bought {quantity} x {item}/s")
# print(f"for ${total}")

# A = input("enter an object: ")
# B = input("enter a verb: ")
# C = input("enter a verb: ")
# D = input("enter a noun: ")
#
# print(f"Life sometimes throws {A} at your door step")
# print(f"if you {B} that dont {C} it")
# print(f"it all was in the {D}")
import math
# radius = float(input("Enter radius: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is: {circumference}")



# R = float(input("Enter Radius: "))
# A = math.pi * pow(R,2)
# print(f"{round(A, 2)}")

# c=a²+b²
#
# A = float(input("enter A: "))
# B = float(input("enter b: "))
# C = math.sqrt(pow(A, 2)+pow(B, 2))
# print(C)



# Response = input("Enter yes or no: ")
#
# if Response == yes:
#     print("you got it sir")
# else:
#     print("ok thanks for answering")

# name = input("Enter your name: ")
#
# if name == "":
#     print("you did not enter your name")
# else:
#     print(f"hello {name}")

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

#TODO:weight converter


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

# #TODO not-inverts boolean , OR-at least one condition should be True, AND- both the condition should be True
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
# #todo if else - terenary
#
# age = 25
#
# print("you are a" + ("child" if age < 18 else "n adult"))

#todo string methods

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

# name = input("Enter your name: ")
#
# result = name.isalpha(), len(name) <= 12
# print(result)

# name = input("Enter your name: ")
#
# if name.isalpha():
#     print("your name is valid")
# elif len(name) <= 12:
#     print("your name is valid")
# else:
#     print("your name is invalid")
#     print(name)

# name = "kumaran"

# print(name[0])
# print(name[0:6])
# print(name[:7])
# print(name[5:])
# print(name[-4])
# print(name[::3])
# print(name[::-1])
# result = name[-4:]
# print(f"your name is {result}")

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

# num = int(input("Enter a number between 1 and 10: "))
#
# while num < 1 or num > 10:
#     print("you have entered the wrong number")
#     num = int(input("Enter a number between 1 and 10: "))
# print(f"your number is {num}")

# 0
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

#todo import time

import time

x = int(input("Enter time: "))
time.sleep(x)
print(x)













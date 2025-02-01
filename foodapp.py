#todo food self-order program
import math

Menu = {"Icecream": 100,
        "Fries": 150,
        "Burger": 200,
        "Pizza": 250,
        "Drinks": 300}

Order = []
total = 0

print("---------------")
for key, value in Menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------")

while True:
    food = input("Enter food name: ").capitalize()  # Convert input to match the case of dictionary keys
    if food == "Q":  # Quit condition
        print("Thank you for your order")
        break
    elif Menu.get(food) is not None:  # todo this will check if food is not there then will return none or not take into account
        Order.append(food)  # todo bring the food into the order list given by user
    else:
        print(f"{food} is not on the menu. Please try again.")

print("---your food----")
for food in Order:
    total += value  # todo total = total + Menu[food]
    print(food, end=" ")

print(f"\ntotal: {total:.2f}")



#todo exception - An event that interrupts the normal flow of the program
#todo             (ZeroDivisionError, TypeError, ValueError)
#todo             1.try 2.except 3.finally

#todo 1 / 0  ZeroDivisionError
#todo "Hello" + 10   TypeError: can only concatenate str (not "int") to str
#todo [1, 2, 3] + "4"   TypeError: can only concatenate list (not "str") to list
#todo int("name")  valueerror # TypeError: can only concatenate

try:
    num = int(input("enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("Invalid operation. Please ensure the inputs are valid.")
finally:
    print("This code block will always execute.")


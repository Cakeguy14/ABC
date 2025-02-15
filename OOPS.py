#todo OOPS concept:
#todo object - a "bundle" of related attributes(variables) and methods(functions)
#todo         ex.phone, cup, book
#todo         you need a "class" to create any objects
#todo class - (blueprint) used to design the structure and layout of the object
#todo methods are different from functions

from OOPS_class_file import Phone

# class Phone:
#     def __init__(self, brand, model, colour, price):
#         self.brand=brand
#         self.model=model
#         self.colour=colour
#         self.price=price

phone1=Phone("Apple","iPhone 12","Black","Rs 100,000")
phone2=Phone("Samsung","Galaxy S21","Blue","Rs 100,000")

phone1.sold()
phone2.not_sold()
phone1.display()

print(phone1.brand)
print(phone1.model)
print(phone1.colour)
print(phone1.price)

print(phone2.brand)
print(phone2.model)
print(phone2.colour)
print(phone2.price)
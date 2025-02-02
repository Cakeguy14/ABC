
#todo iterables - An object or element returns its element one at a time
# allowing it to be iterated over in a loop


numbers = [1,2,3,4,5,6,7,8,9,10]

for i in reversed(numbers):
    print(i)

numbers = (1,2,3,4,5,6,7,8,9,10)

for i in numbers:
    print(i)

fruit = {"apple","banana","cherry"}  #todo you cannot reverse a set
for i in fruit:
    print(i)
#todo Inheritance - allows a class to inherit attributes and methods from another class
#todo               helps with code resusability and extensibility
#todo			    class child(parent)


class pets:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name,"is walking")
    def eat(self):
        print(self.name,"is eating")

class dog(pets):
    pass
class cat(pets):
    pass
class hamster(pets):
    pass

dog = pets("dog","10")
cat = pets("cat","5")
hamster = pets("hamster","3")

print(dog.name)
print(dog.age)
dog.walk()
dog.eat()

print(cat.name)
print(cat.age)
cat.walk()
cat.eat()

print(hamster.name)
print(hamster.age)
hamster.walk()
hamster.eat()
#todo duck typing - another way to use polymorphism
#todo               objects must have minimum necessary attributes/methods
#todo               "if it looks like a duck and quacks like a duck, it must be a duck"

class animal:

    alive = True

class duck(animal):
    def speak(self):
        print("Quack Quack")

class bird(animal):
    def speak(self):
        print("Chirp Chirp")

class fish(animal):

    alive = False
    def speak(self):
        print("Bite Bite")

animals = [duck(), bird(), fish()]

for animal in animals:
    print(animal.alive)
    animal.speak()

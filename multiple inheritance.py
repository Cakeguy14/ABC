#todo multiple inheritance - inherit from more than one parent class
#todo                        C(A, B)
#todo multilevel inheritance - inherit from a parent which inherits from another parent
#todo                          C(B) <- B(A) <- A


class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

class prey(animal):
    def flee(self):
        print(self.name, "is fleeing")
class predator(animal):
    def hunt(self):
        print(self.name, "is hunting")

class duck(prey):
    pass
class horse(prey):
    pass
class lion(predator):
    pass
class rat(prey, predator):
    pass

duck = duck("duck")
horse = horse("horse")
lion = lion("lion")
rat = rat("rat")

print(duck.name)
print(horse.name)
print(lion.name)
print(rat.name)

duck.eat()
duck.flee()
lion.flee()


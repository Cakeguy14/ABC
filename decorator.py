#todo Decorator - A function that extends the behaviour of another function
#todo             w/o modifying the base function
#todo             pass the base function as an argument to the decorator
#todo             @add_sprinkles
#todo             get_ice_cream("vanilla")


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Getting {flavor} ice cream...")

get_ice_cream("chocolate")


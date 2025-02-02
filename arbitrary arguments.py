#todo args

# def add(*args):
#     print(sum(args))
#     return

# add(1,2,3,4,5)

# def user_name(*args):
#     for name in args:
#         print(name, end=" ")
# user_name("senthur","kumar","M")

# def user_name(**kwargs):
#     for name,age in kwargs.items():
#         print(name,age, end=" ")
# user_name(senthur=20)

# def user_name(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value, end=" ")
# user_name(senthur=20)
#
# def user_name(**kwargs):
#     for key, value in {'senthur': 20}.items():
#         print(f"{key}: {value}")
# user_name(senthur=20)

# def user_name(*args,**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# user_name(senthur=20,kumar=25,M=26)

def user_name(*args,**kwargs):
    for args in args:
        print(args, end=" ")
    print()

    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    if kwargs.get('zipcode'):
        print(f"zipcode: {kwargs.get('zipcode')}")
    if kwargs.get('city'):
        print(f"city: {kwargs.get('city')}")
    else:
        print("No city or zipcode")
    # print(f"{kwargs.get('street')} {kwargs.get('city')}")   #todo when using key within kwargs use only '' single quotes
user_name("Mr.","Senthur","Kumaran","M",
          age=20,
          street="123 Main St",
          city="New York",
          zipcode="10001")




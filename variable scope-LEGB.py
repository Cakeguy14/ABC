#todo variable scope - where a variable is visible and accesible
#todo scope resolution - (LEGB) local > enclosed > global > built in


#todo exapmle of local
# def func1():
#     x = 10
#     print(x)
#
# def func2():
#     x = 20
#     print(x)
#
# func1()
# func2()

#todo example of enclosed

# def func3():
#     x = 30
#     def func4():
#         nonlocal x
#         x = 40
#         print(x)
#     func4()
#     print(x)

# def func3():
#     x = 30
#     def func4():
#         print(x)
#
# func3()
#
# #todo example of global
#
# def func5():
#     print(x)
#
# def func6():
#     print(x)
# x= 50
# func5()
# func6()
#
# #todo example of built in
#
# from math import pi
#
# def func7():
#     print(pi)
#
# pi = 3.14
# func7()

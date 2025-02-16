#todo static method - a method belongs to a class rather than any object from that class (instance)
#todo                 usually used for general utility function
#todo instance methods - best for operations on instances of the class(object)
#todo static methods - best for utility function that do not need access to class data

class Employee:
    def __init__(self, name, Position):
        self.name = name
        self.Position = Position

    def details(self):
        return f"{self.name} = {self.Position}"  #todo instance method

    @staticmethod
    def is_valid_position(position):
        is_valid_position = ["manager", "engineer", "salesman"]     #todo static method
        return position in is_valid_position

employee1 = Employee("John", "manager")
employee2 = Employee("Jane", "engineer")
employee3 = Employee("Mike", "salesman")

print(Employee.is_valid_position("manager"))
print(employee1.details())
print(employee2.details())
print(employee3.details())



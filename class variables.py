#todo class variables - shared among all instances of a class
#todo                   defined outside the constructor
#todo				   allows you to share data among all objects created from that class

class student:

    graduation_year=2025  #todo class variable outside the constructor
    num_students=0

    def __init__(self,name,age):    #todo constructor
            self.name=name          #todo instance variable inside the constructor
            self.age=age
            student.num_students += 1

student1=student("John",20)
student2=student("Jane",21)
print(f"Number of students: {student.num_students} graduation year: {student.graduation_year}")
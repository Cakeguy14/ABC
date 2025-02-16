#todo class methods - allow operations related to the class itself
#todo                 Take(cls) as the first parameter, which represent the class itself


class student:

    count = 0
    total_gpa = 0.0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        student.count += 1
        student.total_gpa += gpa

    def display(self):
        return f"Student name: {self.name}, Student age: {self.gpa}"

    def get_count(cls):
        return f"Total students: {cls.count}"

    def get_total_gpa(cls):
        return f"total gpa: {cls.total_gpa/cls.count}"

student1=student("John",3)
student2=student("Jane",4)

print(student1.display())
print(student2.display())
print(student.get_count(student))
print(student.get_total_gpa(student))
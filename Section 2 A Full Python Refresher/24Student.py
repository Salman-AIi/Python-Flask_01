import statistics
import math
import random

class Student:

    def __init__(self,name,University):
        self.name = name
        self.University = University
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks)
        


anna = Student('Anna','MIT')
anna.marks.append(25)
anna.marks.append(56)
print(anna.marks)

print(anna.average())
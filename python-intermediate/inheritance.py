class Empolyee:
    start_time="10am"
    end_time="6pm"

class Teacher(Empolyee):
    #now class teacher has all the properties stated in class Employee because teacher is also an employee
    def __init__(self,subject):
        self.subject=subject

Ruma = Teacher("English")#Ruma is a teacher and further an employee

print(Ruma.start_time,Ruma.end_time,Ruma.subject)

        
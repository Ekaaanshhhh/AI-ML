class Student:
    subject="Python"
#this is what our Student class ke objects ka blueprint looks like

stu1 = Student();#stu1 is an object of class Student
#stu1 will also have the property of subject fixed as "python"

print(stu1.subject)


stu2 = Student();#another object of class Student but stu1 and stu2 have different memory addresses

#can also have functions
# class info:
#     name=""
#     grade=0
#     section=""
#     def greet():
#         print(f"welcome, my name is {name} , my class is section {section} and grade is {grade}")
    
# ekansh = info();
# ekansh.name="ekansh",
# ekansh.grade=8.7
# ekansh.section="a"

# ekansh.greet();
#THIS WILL NOT WORK WITHOUT A CONSTRUCTOR



#constructor
#created using the word init
class info:
    def __init__(self,name,grade,section):
        self.name=name
        self.grade=grade
        self.section=section
    def greet(self):
       return self.name

ekansh = info("ekansh",8.7,"a")
obj = ekansh.greet()
print(f"Welcome, i am {obj} ")


#dewfault constructor has only self parameter in it and paramterized has self and also other parameters



#CLASS AND ATTRIBUTES
#class attribute - belongs to class and is common for all objects
#instance/object attribute - belongs to object and is unique for each object
#to save time, jo bhi common attributes hote hai usko hum class attribute bana dete hai aur baaki sabko jo change hote hai unko instance attributes bana dete hai

class college:
    name="NITP"
    def __init__(self,stuname,stubranch):
        self.stuname=stuname,
        self.stubranch=stubranch,

student1 = college("ekansh","ece")
#here name of college i.e nitp will be common to all students studying here so it will be a class attribute
#and the stuname i.e student name and stubranch will vary with each student so it is an object attribute
print(student1.name)#name of college i.e class attribute
print(student1.stuname)#name of student i.e object attribute
print(student1.stubranch)#name of the branch i.e object attribute

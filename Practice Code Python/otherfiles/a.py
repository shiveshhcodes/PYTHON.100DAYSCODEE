# def new_func():
#     class Employee:
#       def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     class Programmer(Employee):
#       def __init__(self, name, id, lang):
#         super().__init__( name, id)
#         self.lang = lang

#     rohan = Employee("Rohan Das", "420")
#     harry = Programmer("Harry", "2345", "Python")
#     print(harry.name)
#     print(harry.id)
#     print(harry.lang)

# new_func()

# class college:
#   def __init__(self , name , number):
#     self.name = name
#     self.number = int(number)
    
#   def show(self):
#     print(f"{self.name} number is {self.number}")
    
# class classes (college):
#   def __init__(self, name, number , section):
#    super().__init__(name, number)
#    self.section = section
   
#   def show1(self):
#     print(f"{self.name} number is not {self.number}")
   
# college_name = college("IPS" , 21)
# classes_name = classes("DS" , 212 , "D" m)
# classes_name2 = college("DS1" , 2112)

# # print(classes_name2.name)
# college_name.show()
# classes_name.show1()
# classes_name2.show()
class college:
    def __init__(self, name, number):
        self.name = name
        self.number = int(number)
    
    def show(self):
        print(f"{self.name} number is {self.number}")
        
        
    def __str__(self):
        return f"the name iss {self.name} and the number is {self.number}"
    
    def __len__(self):
     i = 0 
     for a in self.name:
      i = i+1
     return i

class classes(college):
    def __init__(self, college_instance, section):
        self.name = college_instance.name
        self.number = college_instance.number
        self.section = section
   
    def show1(self):
        print(f"{self.name} number is {self.number} and section is {self.section}")

college_name = college("IPS", 21)
classes_name = classes(college_name, "D")
# college_len = college("hello" , 23)
# print(len(college_len))

college_name.show()
classes_name.show1()
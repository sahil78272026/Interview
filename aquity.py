# Company - Aquity
# HR - Reena T , 08667320835
# First Round


"""# 
def greet(name):
    return "Hi " + name
    


def greet2(name1 , name2):
    return "Hi " + name1 + name2


print(greet2('Sanjeth ',' Sahil'))"""


"""def capitalize(func):
    def wrapper_func(*args):
        return func(*args).upper()
    return wrapper_func


@capitalize
def greet(name):
    return f"Hi {name}"
 
@capitalize
def greet2(name1, name2):
    return f"Hello {name1} and {name2}"

print(greet("Sahil"))
print(greet("Sahil","Sanjeth"))
"""




"""class A:
    def __init__(self, a,b):
        self.main_var = a + b
    
    def get_output(self):
        return f"the main_var from parent a is {self.main_var}"
 
class B:
    def __init__(self, a,b):
        self.main_var = a * b
    
    def get_output(self):
        return f"the main_var from parent b is {self.main_var}"       
 
class c(A,B):
    def __init__(self, a,b):
        self.main_var = 3


    pass
 
c_object = c(2,3)
print(c_object.get_output()) # 3
"""

"""class Vector: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self,other):
        return Vector(self.x-other.x , self.y-other.y)
    
        


    
v2 = Vector(6,7)
v1 = Vector(5,3)

# print(dir(v2))

print(v2-v1)
"""

"""newL = [num*3 for num in range(0,101) if num%2==0] 
print(newL)"""

# id, name, subject

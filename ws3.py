#1. Write a Python function to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference. 

def diff17(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
print(diff17(22))
print(diff17(14))

#  2. Write a Python function test_range(n) that returns True if the number is within 1001000 or 2000, otherwise returns False. 

def test_range(n):
    return (n in range(100,1001)) or (n == 2000)
print(test_range(150))
print(test_range(2500))

# 3. Write a Python function to reverse a string. Example: Input = 'robot', Output = 'tobor’. 

def reverse_string(s):
    return s[::-1]
print(reverse_string("robot"))

# 4. Write a Python function that accepts a string and counts the number of uppercase and lowercase letters. Return the counts as a dictionary. 

def count_case(s):
    d = {"UPPER":0, "LOWER":0}
    for c in s:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
    return d
print(count_case("ROBOTICSandAI"))

# 5. Write a Python function that takes a list and returns a new list with distinct elements from the first list. 

def unique_list(lst):
    new = []
    for x in lst:
        if x not in new:
            new.append(x)
    return new
print(unique_list([1,2,2,3,4,4,5]))

# 6. Write a Python program to return the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]        Expected Result : [2, 4, 6, 8] 
def even_numbers(lst):
    res = []
    for n in lst:
        if n % 2 == 0:
            res.append(n)
    return res
print(even_numbers([1,2,3,4,5,6,7,8,9]))

# 7. Write a Python program to define a function inside another function and call it. Example: Outer function = robot(), Inner function = move(). 
def robot():
    def move():
        print("moving")
    move()
robot()

# 8. Define a Python function student(name, age, course). Using function attributes, display the names of all arguments. 
def student(name, age, course):
    return name, age, course
print(student.__code__.co_varnames)

# 9. Write a Python function move_robot(x, y, direction) that takes a robot’s current position (x, y) and a direction ('up', 'down', 'left', 'right'). The function should return the new position of the robot. Example: move_robot(0,0,"up") → (0,1) 

def move_robot(x, y, direction):
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x,y)
print(move_robot(0,0,"up"))
print(move_robot(2,3,"left"))

# 10. Write a Python function classify_temperature(temp) that classifies a robot’s environment:  Return "Cold" if temp < 15 Return "Moderate" if 15 ≤ temp ≤ 30 Return "Hot" if temp > 30 

def classify_temperature(temp):
    if temp < 15:
        return "cold"
    elif 15 <= temp <= 30:
        return "moderate"
    else:
        return "hot"
print(classify_temperature(10))
print(classify_temperature(20))
print(classify_temperature(35))

# 11. Write a Python function is_goal_reached(path) where path is a list of robot moves (["up", "right", "right", "down"]). The function should return True if the final position is at (2,0) starting from (0,0), otherwise False. URA302 | Dr. Rohit Kumar Singla 
def is_goal_reached(path):
    x = 0
    y = 0
    for move in path:
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
    return (x,y) == (2,0)
print(is_goal_reached(["up","right","right","down"]))
print(is_goal_reached(["up","right"]))

# 12. Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class. 

class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
    def display(self):
        print("ID:", self.student_id, "name:", self.student_name, "class:", self.student_class)
s = Student(1,"abc","RAI")
s.display()

# 13. Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format. 
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
student1 = Student(1,"abc","RAI")
student2 = Student(2,"xyz","RAI")
print("ID:", student1.student_id, "name:", student1.student_name, "class:", student1.student_class)
print("ID:", student2.student_id, "name:", student2.student_name, "class:", student2.student_class)

# 14. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle. 
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def perimeter(self):
        return 2 * math.pi * self.r
c = Circle(5)
print(c.area())
print(c.perimeter())

# 15. Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case. 

class StringClass:
    def get_String(self):
        self.s = input("enter a string: ")
    def print_String(self):
        print(self.s.upper())
obj = StringClass()


# 16. Write a Python class named Robot that has attributes: name, task, and battery_level. The class should have methods: perform_task() → Prints the task the robot is performing and decreases the battery by 10%. recharge() → Sets the battery level back to 100%. status() → Prints the robot's name, current task, and battery level.
class Robot:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.batterylevel = 100
    def perform_task(self):
        print(self.name, "is performing:", self.task)
        self.batterylevel -= 10
    def recharge(self):
        self.batterylevel = 100
    def status(self):
        print("name:", self.name, "task:", self.task, "battery:", self.batterylevel)
r = Robot("robo","cleaning")
r.perform_task()
r.status()
r.recharge()
r.status()
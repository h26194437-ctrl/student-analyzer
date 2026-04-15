# functions.py

from constants import *

def calculate_grade(avg):
    for grade, boundary in GRADE_BOUNDARIES.items():
        if avg >= boundary:
            return grade

def add_student(students):
    name = input("Enter name: ")
    subjects = int(input("Enter number of subjects: "))
    
    marks = []
    for i in range(subjects):
        m = float(input(f"Enter marks {i+1}: "))
        marks.append(m)

    students[name] = {"marks": marks}

def compute_results(students):
    for name in students:
        marks = students[name]["marks"]
        avg = sum(marks) / len(marks)
        students[name]["average"] = avg
        students[name]["grade"] = calculate_grade(avg)

def display_all(students):
    compute_results(students)
    
    for name, data in students.items():
        print(SEPARATOR)
        print("Name:", name)
        print("Marks:", data["marks"])
        print("Average:", data["average"])
        print("Grade:", data["grade"])

def find_topper(students):
    compute_results(students)
    topper = max(students.items(), key=lambda x: x[1]["average"])
    print("Topper:", topper)

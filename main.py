# main.py

from functions import *
from constants import *

students = {}

print(WELCOME_MESSAGE)

while True:
    print(SEPARATOR)
    for option in MENU_OPTIONS:
        print(option)

    choice = input("Enter choice: ")

    if choice == '1':
        add_student(students)

    elif choice == '2':
        display_all(students)

    elif choice == '3':
        find_topper(students)

    elif choice == '0':
        break

    else:
        print("Invalid choice")

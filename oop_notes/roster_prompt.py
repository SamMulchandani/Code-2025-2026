# create a repeating menu that prompts the user for a choice

# the menu printed should look like the following
# (o)pen file
# (v)iew roster
# (q)uit program

from roster import *


roster = Roster()

cont = True
while(cont):
    choice = input("What would you like to do?\n(a)dd student\n(o)pen file\n(s)ave file\n(v)iew roster\n(q)uit program\n") 
    if choice == "a":
        first = input("First name? ")
        last = input("Last name? ")
        grade = int(input("Grade? "))
        s = Student(first,last,grade)
        roster.students.append(s)

    elif choice == "o":
        file = input("Filename?")
        roster.load(file)
        print("Opening file...")
        print(f"{file} loaded successfully...")

    elif choice == "s":
        pass

    elif choice == "v":
        print(roster)

    elif choice == "q":
        cont = False
        
    else:
        print("Invalid choice. Please try again")

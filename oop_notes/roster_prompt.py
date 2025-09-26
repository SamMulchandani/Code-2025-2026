# create a repeating menu that prompts the user for a choice

# the menu printed should look like the following
# (o)pen file
# (v)iew roster
# (q)uit program

from roster import *


roster = Roster()

cont = True
while(cont):
    choice = input("What would you like to do?\n(a)dd student\n(o)pen file\n(s)ave file\n(v)iew roster\n(q)uit program\n>> ") 
    if choice == "a":
        first = input("First name? ")
        last = input("Last name? ")
        grade = int(input("Grade? "))
        roster.add_student_by_info(first,last,grade)
        print("")

    elif choice == "o":
        file = input("Filename? ")
        roster.load(f"oop_notes/{file}")
        print(f"{file} loaded successfully...\n")

    elif choice == "s":
        save_file = input("Save to where? ")
        roster.save(f"oop_notes/{save_file}")
        print(f"{save_file} saved successfully...\n")

    elif choice == "v":
        print(roster)
        print("")
        
    elif choice == "q":
        cont = False

    else:
        print("Invalid choice. Please try again\n")

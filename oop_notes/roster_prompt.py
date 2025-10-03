# create a repeating menu that prompts the user for a choice

# the menu printed should look like the following
# (o)pen file
# (v)iew roster
# (q)uit program

from roster import *


roster = Roster()

cont = True
while(cont):
    choice = input("What would you like to do?\n(a)dd student\n(e)dit student\n(r)emove student\n(f)ind student\n(o)pen file\n(s)ave file\n(so)rt by first name\n(v)iew roster\n(q)uit program\n>> ") 
    if choice == "a":
        first = input("First name? ")
        last = input("Last name? ")
        grade = int(input("Grade? "))
        roster.add_student_by_info(first,last,grade)
        print("")

    elif choice == "e":
        first = input("First name of student? ")
        last = input("Last name of student? ")
        if roster.find(first,last) is not None:
            new_first = input("New first name of student? (If not changing leave blank)\n")
            new_last = input("New last name of student? (If not changing leave blank)\n")
            new_grade = input("New grade of student? (If not changing enter -1)\n")
            roster.find_and_edit_info(first, last, new_first, new_last, new_grade)
            print("Student updated successfully...\n")
        else:
            print("Student not found...\n")

    elif choice == "r":
        first = input("First name of student? ")
        last = input("Last name of student? ")
        removed = roster.remove_student(first,last)
        if removed is None:
            print(f"{first} {last} was not found...\n")
        else:
            print(f"{first} {last} was removed successfully...\n")

    elif choice == "f":
        first = input("First name of student? ")
        last = input("Last name of student? ")
        print(roster.find_and_display_info(first,last))
        print()

    elif choice == "o":
        file = input("Filename? ")
        roster.load(f"oop_notes/{file}")
        print(f"{file} loaded successfully...\n")

    elif choice == "s":
        save_file = input("Save to where? ")
        roster.save(f"oop_notes/{save_file}")
        print(f"{save_file} saved successfully...\n")

    elif choice == "so":
        roster.selection_sort_by_first_name()
        print("List sorted by first name successfully...\n")

    elif choice == "v":
        print(roster)
        print("")
        
    elif choice == "q":
        cont = False

    else:
        print("Invalid choice. Please try again\n")

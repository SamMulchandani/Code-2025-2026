from student import *
class Roster:

    def __init__(self):
        self.students = []

    def __str__(self):
        s = ""
        for student in self.students:
            s += student.first + " " + student.last + "\n"
        return s
    
    def add_student_by_info(self, first, last, grade):
        self.students.append(Student(first,last,grade))

    # opens and reads the filename and
    # loads students with Student obejects
    def load(self, filename):
        #open file
        # file = open(filename, "r")
        #read in data
        # data = file.read() #read entire file into a single string
        # data = file.readline() #read a single line from file
        # data = file.readlines() #read entire file into single list
        # line = "line"
        # while line:
        #     line = file.readline().strip()
        #     if not line:
        #         break
        self.students = []
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                s = Student(parts[0], parts[1], int(parts[2]))
                self.students.append(s)
            

        #close file
        # file.close()
        #split line-by-line and create Student

    def save(self,filename):
        with open(filename, "w") as file:
            for student in self.students:
                file.write(f"{student.first},{student.last},{student.grade}\n")

# my_roster = Roster()
# my_roster.load("oop_notes/data.csv")
# print(my_roster)
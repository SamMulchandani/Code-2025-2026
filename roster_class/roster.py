from oop_notes.student import *
class Roster:

    def __init__(self):
        self.students = []

    def __str__(self):
        pass

    # opens and reads the filename and
    # loads students with Student obejects
    def load(self, filename):
        #open file
        file = open(filename, "r")
        #read in data
        # data = file.read() #read entire file into a single string
        # data = file.readline() #read a single line from file
        # data = file.readlines() #read entire file into single list
        line = "line"
        while line:
            line = file.readline().strip()
            if not line:
                break
            parts = line.split(",")
            s = Student(parts[0], parts[1], int(parts[2]))
            self.students.append(s)
            

        #close file
        file.close()
        #split line-by-line and create Student


my_roster = Roster()
my_roster.load("data.csv")
print(str(my_roster.students))
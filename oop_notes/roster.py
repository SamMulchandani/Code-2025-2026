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

    def remove_student(self, first, last):
        for i in range(len(self.students)):
            if self.students[i].first == first \
            and self.students[i].last == last:
                return self.students.pop(i)
        return None

    def find(self, first, last):
        for i in range(len(self.students)):
            if self.students[i].first == first \
            and self.students[i].last == last:
                return self.students[i]
        return None
    
    def find_and_display_info(self, first, last):
        found = self.find(first, last)
        if found is None:
            return f"{first} {last} was not found..."
        else:
            return f"First name: {first}\nLast name: {last}\nGrade: {found.grade}"

    def find_and_edit_info(self, first, last, new_first, new_last, new_grade):
        found = self.find(first, last)
        if found is not None:
            if new_first != "":
                found.first = new_first
            if new_last != "":
                found.last = new_last
            if new_grade != -1:
                found.grade = new_grade

    def selection_sort_by_first_name(self):
        # Initialize a counter variable to remember the front index
        # Use the front counter variable to iterate through the array with a loop, and during each iteration…
        for front in range(len(self.students)):
            # Initialize a variable to remember the minimum element's index
            min = front
            # Use another loop with a different counter variable to iterate from the front to the end of the array (i.e. initialize this loop's counter using front)
            for i in range(front, len(self.students)):
            # Within this inner loop, find the index of the minimum element in the unsorted region
                if self.students[i].first < self.students[min].first:
            # Compare each element to the current minimum, and if it is smaller, update the current minimum's index
                    min = i
            # After the inner loop, we can swap the minimum element with the front element
            temp = self.students[front]
            self.students[front] = self.students[min]
            self.students[min] = temp

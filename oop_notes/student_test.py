from student import Student

def list_students_last_names(roster):
    for student in roster:
        print(student.last)


student_1 = Student("sam", "mulchandani", 12)
student_2 = Student("student2", "lastname", 1)
student_3 = Student()

test = student_1

print(student_1)
# print(test)
# print(student_2)

student_1.sayHello()
# student_2.cast("spell")
student_1.cast("evil spell", student_2)

print("")

my_list = []
my_list.append(student_1)
my_list.append(student_2)

list_students_last_names(my_list)

print(f"\nStudent 3: {student_3}")
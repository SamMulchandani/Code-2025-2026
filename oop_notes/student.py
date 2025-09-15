class Student:
    #static class variables (Shared by instances)
    #no class variables for now

    #init() that initializes instance variables
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    #methods()
    def __str__(self):
        return (self.first + " " + self.last + " is in Grade " + str(self.grade))
    
    def sayHello(self):
        print(f"{self.first} says hello!")

    # def cast(self, spell):
    #     print(f"{self.first} casts {spell}")

    def cast(self, spell: str, other: "Student"):
        print(f"{self.first} casts {spell} at {other.first}")


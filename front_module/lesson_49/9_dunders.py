
class Journal:

    def __init__(self):
        self.students = []
    
    def __iter__(self):
        for student in self.students:
            print(f"before: {student}")
            
            yield student

            print(f"after: {student}")


    def __call__(self):
        print("test test test __Call_ method!")




journal = Journal()

journal[0]

a = ["Ulan", "German", "Alua", "Almas"]

print(type(a))
# journal.students = ["Ulan", "German", "Alua", "Almas"]

# for student in journal:
#     print(student)







class Animal:
    cnt = 0
    age = 1
    name = "Ulan"
    surname = "Qospan"

    @property
    def full_name(self):
        return f"{Animal.name} {Animal.surname}"


    def __init__(self):
        Animal.cnt += 1




a = Animal()

print(a.full_name)


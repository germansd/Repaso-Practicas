class Person:
    def __init__(self, name, surname):  # Sí o sí ponemos el self
        self.fullname = name + surname
        self.name=name

    def walk(self):  # Sí o sí ponemos el self
        print(f"{self.fullname} anda")

    def get_name(self):
        return self.name
    
persona = Person("German ", "Sanchez")

print(persona.fullname)
persona.walk()
print(persona.get_name())
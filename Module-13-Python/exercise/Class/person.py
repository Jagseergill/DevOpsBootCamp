class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

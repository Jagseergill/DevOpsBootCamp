class Lecture:
    def __init__(self, name, max_students, duration, professors):
        self.name = name
        self.max_students = max_students
        self.duration_minutes = duration
        self.professors = professors

    def print_name_and_duration(self):
        print(f"{self.name} - {self.duration_minutes} minutes")

    def add_professors(self, new_professor):
        self.professors.append(new_professor)

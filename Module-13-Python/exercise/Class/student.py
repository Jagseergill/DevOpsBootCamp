from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def list_lectures(self):
        print("Attends lectures:")
        for lecture in self.lectures:
            print(f"- {lecture.name}")

    def attend_lecture(self, new_lecture):
        self.lectures.append(new_lecture)

    def leave_lecture(self, lecture):
        self.lectures.pop(lecture)

from professor import Professor
from student import Student
from lecture import Lecture

cs_lecture = Lecture("Computer science", 15, 45, [])
python_basics_lecture = Lecture("Python programming basics", 25, 90, [])
python_advanced_lecture = Lecture("Python advanced", 10, 90, [])
algorithms_lecture = Lecture("Algorithms and data sturctures", 30, 120, [])

new_professor = Professor("Maria", "Smith", 34, [cs_lecture, python_basics_lecture])
new_professor.print_full_name()
new_professor.teach_lecture(python_advanced_lecture)
new_professor.list_lectures()

cs_lecture.add_professors(new_professor)
python_basics_lecture.add_professors(new_professor)
python_advanced_lecture.add_professors(new_professor)

print("------------------------------")

new_student = Student("David", "Green", 25, [algorithms_lecture])
new_student.print_full_name()
new_student.attend_lecture(python_basics_lecture)
new_student.list_lectures()

print("------------------------------")

cs_lecture.print_name_and_duration()
python_basics_lecture.print_name_and_duration()

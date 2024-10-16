class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print(f"Не могу оценить лектора {lecturer.name} {lecturer.surname} по курсу {course}.")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print(f"Не могу оценить студента {student.name} {student.surname} по курсу {course}.")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 9)

print(f'Оценки лектора {cool_lecturer.name} {cool_lecturer.surname}: {cool_lecturer.grades}')

cool_reviewer = Reviewer('Ann', 'Smith')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_student(best_student, 'Python', 10)

print(f'Оценки студента {best_student.name} {best_student.surname}: {best_student.grades}')

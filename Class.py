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

    def average_grade(self):
        if self.grades:
            return round(sum([sum(grades) for grades in self.grades.values()]) / 
                         sum([len(grades) for grades in self.grades.values()]), 1)
        return 0.0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades:
            return round(sum([sum(grades) for grades in self.grades.values()]) / 
                         sum([len(grades) for grades in self.grades.values()]), 1)
        return 0.0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print(f"Не могу оценить студента {student.name} {student.surname} по курсу {course}.")

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10]
best_student.grades['Python'] = [9, 8]

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.grades['Python'] = [9, 9, 10]

cool_reviewer = Reviewer('Ann', 'Smith')
cool_reviewer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

print(best_student < Student('John', 'Doe', 'your_gender')) 
print(cool_lecturer < Lecturer('Jane', 'Doe')) 

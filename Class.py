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

def average_student_grade(students, course): # Функция для подсчета средней оценки
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total_grade / count, 1) if count else 0.0

def average_lecturer_grade(lecturers, course): # Функция для подсчета средней оценки за лекции по курсу
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total_grade / count, 1) if count else 0.0
    
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Python']
student_1.grades['Git'] = [9, 9, 9]
student_1.grades['Python'] = [8, 9]

student_2 = Student('John', 'Doe', 'male')
student_2.finished_courses += ['Git']
student_2.courses_in_progress += ['Python']
student_2.grades['Git'] = [8, 8, 8]
student_2.grades['Python'] = [10, 9]

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.grades['Python'] = [9, 10, 10]

lecturer_2 = Lecturer('Jane', 'Doe')
lecturer_2.courses_attached += ['Python']
lecturer_2.grades['Python'] = [8, 9, 9]

reviewer_1 = Reviewer('Ann', 'Smith')
reviewer_1.courses_attached += ['Python']
reviewer_1.rate_student(student_1, 'Python', 9)
reviewer_1.rate_student(student_2, 'Python', 8)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)

# средняя оценка за дз
average_student = average_student_grade([student_1, student_2], 'Python')
print(f'Средняя оценка студентов за курс Python: {average_student}')

# средняя оценка за лекции
average_lecturer = average_lecturer_grade([lecturer_1, lecturer_2], 'Python')
print(f'Средняя оценка лекторов за курс Python: {average_lecturer}')

class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def midgrade(self, grade):
        summary_grade = []
        for val in grade.values():
            for v in val:
                summary_grade.append(v)
        mg = sum(summary_grade)/len(summary_grade)
        return mg

    def rate_ws(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.l_grades:
                lecturer.l_grades[course] += [grade]
            else:
                lecturer.l_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        summary_grade = []
        for val in self.grades.values():
            for v in val:
                summary_grade.append(v)
        info = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.midgrade(self.grades):.{1}f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return info

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.midgrade(self.grades) < other.midgrade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.l_grades = {}
        Lecturer.lecturer_list.append(self)

    def __str__(self):
        summary_rate = []
        for val in self.l_grades.values():
            for v in val:
                summary_rate.append(v)
        info = f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {(sum(summary_rate)/len(summary_rate)):.{1}f}'
        return info

    def midrate(self, rate):
        summary_rate = []
        for val in rate.values():
            for v in val:
                summary_rate.append(v)
        mg = sum(summary_rate)/len(summary_rate)
        return mg

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.midrate(self.l_grades) < other.midrate(other.l_grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'\nИмя: {self.name}\nФамилия: {self.surname}'
        return info


the_best_student = Student('Koko', 'Channel', 'your_gender')
the_best_student.courses_in_progress += ['Python']
the_best_student.courses_in_progress += ['Git']
the_best_student.finished_courses += ['Введение в программирование']
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_reviewer = Reviewer('Any', 'Body')
cool_lecturer = Lecturer('No', 'One')
the_cool_lecturer = Lecturer('For', 'Tune')

cool_lecturer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
the_cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
the_cool_lecturer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Git', 6)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(the_best_student, 'Git', 5)
cool_reviewer.rate_hw(the_best_student, 'Git', 6)
cool_reviewer.rate_hw(the_best_student, 'Git', 5)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(the_best_student, 'Python', 9)
cool_reviewer.rate_hw(the_best_student, 'Python', 8)
cool_reviewer.rate_hw(the_best_student, 'Python', 10)

best_student.rate_ws(cool_lecturer, 'Git', 9)
best_student.rate_ws(cool_lecturer, 'Git', 8)
best_student.rate_ws(cool_lecturer, 'Git', 9)
best_student.rate_ws(the_cool_lecturer, 'Git', 8)
best_student.rate_ws(the_cool_lecturer, 'Git', 7)
best_student.rate_ws(the_cool_lecturer, 'Git', 6)
best_student.rate_ws(cool_lecturer, 'Python', 9)
best_student.rate_ws(cool_lecturer, 'Python', 10)
best_student.rate_ws(cool_lecturer, 'Python', 9)
best_student.rate_ws(the_cool_lecturer, 'Python', 8)
best_student.rate_ws(the_cool_lecturer, 'Python', 7)
best_student.rate_ws(the_cool_lecturer, 'Python', 6)


def midgrade_for_course(st_list, a_course):
    st_grades = []
    for student in st_list:
        for course, grade in student.grades.items():
            if course == a_course:
                st_grades.extend(grade)
    mfc = sum(st_grades) / len(st_grades)
    return mfc


def midrate_for_course(st_list, a_course):
    st_rates = []
    for lecturer in st_list:
        for course, rate in lecturer.l_grades.items():
            if course == a_course:
                st_rates.extend(rate)
    mfc = sum(st_rates) / len(st_rates)
    return mfc


print(f'Средний балл студентов по курсу Git: {midgrade_for_course(Student.student_list, "Git"):.{1}f}\n')
print(f'Средний балл студентов по курсу Python: {midgrade_for_course(Student.student_list, "Python"):.{1}f}\n')
print(f'Средний балл лекторов по курсу Git: {midrate_for_course(Lecturer.lecturer_list, "Git"):.{1}f}\n')
print(f'Средний балл лекторов по курсу Python: {midrate_for_course(Lecturer.lecturer_list, "Python"):.{1}f}\n')

print(the_cool_lecturer < cool_lecturer)
print(the_cool_lecturer > cool_lecturer)
print(best_student < the_best_student)
print(best_student > the_best_student)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

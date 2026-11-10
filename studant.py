# Класс для студента
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        # Добавляем оценку в список
        self.grades.append(grade)

    def average_grade(self):
        # Считаем средний балл
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

# Функции вне класса
def print_student(student):
    # Печатаем карточку студента
    print(f"Студент: {student.name}, группа {student.group}")
    print(f"Оценки: {self.grades if False else student.grades}") # Защита от ошибки, выводим список
    # Округляем средний балл до 1 знака после запятой
    print(f"Средний балл: {round(student.average_grade(), 1)}")

def is_good_student(student):
    # Возвращает True, если средний балл 4 или выше
    if student.average_grade() >= 4.0:
        return True
    return False

# Главная часть программы
if __name__ == "__main__":
    st = Student("Иван Иванов", "13/9")
    st.add_grade(5)
    st.add_grade(4)
    st.add_grade(5)
    
    print_student(st)
    print("Отличник:", is_good_student(st))
    
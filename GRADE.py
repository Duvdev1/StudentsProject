class GRADE:
    grade_current_index = 1
    sum_grades = 0

    def __init__(self, __student_name, __topic, __grade):
        self.__grade_index = GRADE.grade_current_index
        self.__student_name = __student_name
        self.__topic = __topic
        self.__grade = __grade
        GRADE.sum_grades += __grade
        GRADE.grade_current_index += 1

    def get_student_name(self):
        return self.__student_name

    def get_topic(self):
        return self.__topic

    def get_grade(self):
        return self.__grade

    def get_index(self):
        return self.grade_current_index

    def set_student_name(self, new_name):
        self.__student_name = new_name

    def set_topic(self, new_topic):
        valid_topics =  ['python', 'math', 'english']
        if new_topic in valid_topics:
            self.__topic = new_topic

    def set_grade(self, new_grade):
        GRADE.sum_grades -= self.__grade
        self.__grade = new_grade
        GRADE.sum_grades += self.__grade

    @staticmethod
    def get_grade_current_index():
        return GRADE.grade_current_index

    @staticmethod
    def get_sum_grades():
        return GRADE.sum_grades

    @staticmethod
    def get_avg():
        if GRADE.grade_current_index != 0:
            return GRADE.sum_grades / GRADE.grade_current_index
        return None

    def is_grade_higher_than_avg(self):
        return self.get_avg() < self.__grade

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

shalom = GRADE('Shalom', 'x', 95)
shalom1 = GRADE('Shalom1', 'xY', 95)

print(shalom)
print(shalom1)
print(shalom.sum_grades)
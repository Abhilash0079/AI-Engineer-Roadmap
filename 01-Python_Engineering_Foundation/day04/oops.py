class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.score}")

class ExamResult:
    def __init__(self, marks):
        self._marks = marks

    def get_marks(self):
        return self._marks

    def display_result(self):
        print(f"Exam marks: {self._marks}")



student1 = Student("Alex", 85)
student1.display_details()

student2 = Student("Sam", 92)
student2.display_details()

result = ExamResult(85)
print(result.get_marks())
result.display_result()
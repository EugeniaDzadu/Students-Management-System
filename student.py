class Student:
    """
     This is a blueprint of every student object
    """
    def __init__(self, student_id, first_name, last_name, age, gender) :
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        
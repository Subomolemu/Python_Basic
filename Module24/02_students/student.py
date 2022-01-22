class Student:
    def __init__(self, info, group_num, grade_list):
        self.info = info
        self.group_num = group_num
        self.grade_list = grade_list
    
    def sort_student(self):
        score = 0
        for i in self.grade_list:
            score += i
        return score
    
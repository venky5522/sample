class student:
    def __init__(self,stu_name,stu_rollno,stu_grade):
        self.stu_name = stu_name
        self.stu_rollno = stu_rollno
        self.stu_grade = stu_grade
    def get_name(self):
        return self.stu_name
    def get_rollno(self):
        return self.stu_rollno
    def get_grade(self):
        return self.stu_grade
    def get_values(self):
        return '-'.join([self.get_name,str(self.get_rollno),self.get_grade])
obj = student("venkatesh",21,"A")
print(obj.get_name())
print(obj.get_rollno())
#obj.get_values()
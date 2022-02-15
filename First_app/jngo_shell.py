## exec(open(r"C:\Users\pc\studies\Django\first_project\First_app\jngo_shell.py").read())
from First_app.models import Student
import random




#print(Student.average_of_marks())

#Student.conditional_increment_marks()

#Student.add_prefix_to_name()

#Student.get_all_student_details()

#print(Student.delete_id_data())

## -----------------------------
# no_of_stud,studs =Student.count_of_student_wrt_age()
# print(no_of_stud,"\n",studs)

## -------------------------

#print(Student.get_inactive_student())

#Student.fetch_data_from_sql()

###--------------creating object for table Student2 -------------
# def stud():
#     s=""
#     for i in range(random.randint(4,5)):
#         s+=chr(random.randint(65,91))
#     return s.title()
# def student_list(num,cls_name):
    
#     for i in range(num):
#         sl = cls_name(name=stud(),age=random.randint(20,30),marks=random.randint(20,99))
#         sl.save()
    
# studs = student_list(6,Student2)
##---------------------------------------------------------------------

# data = Student.objects.first()
# print(data,type(data))
#s = Princi.objects.create(name="virus")
#c = Student.objects.filter(department__college__name="raisoni")
#print(c)
#print(c.department)
c = Student.person.all()
print(c)



from django.db import models
from functools import reduce

# Create your models here.
class Person(models.Manager):
    '''first we get all objects from the database by
  calling the get_queryset method of the inherited class
  i.e. Manager class using super().get_queryset().
  After that we are filtering objects having city attribute equal to kolkata
  and return the filtered objects'''
    def get_queryset(self):
        return super().get_queryset().filter(id = 2)
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.FloatField()
    is_active = models.BooleanField(default=True)

    

    class Meta :
        db_table = "Students"
    
    person = Person()
    
    def __str__(self) :
        return f"{self.name}"

# ### calculate average marks using reduce()  function
 
#     @classmethod
#     def average_of_marks(cls):
#         l = []
#         data = cls.objects.all()
#         for i in data:
#             l.append(i.marks)
#         average = reduce(lambda x,y:x+y,l)/len(data)
#         return average

# ### increments of marks by 15 percent and keep unchange for those crossing 100 percent after increament

#     @classmethod
#     def conditional_increment_marks(cls):
#         data = cls.objects.all()
#         for i in data:
#             i.marks += (i.marks*15/100)
#             if i.marks < 100:
#                 i.save()
#             else :
#                 pass

# ### get details for all student  using class method         
        
#     @classmethod
#     def get_all_student_details(cls):
#         data = cls.objects.all()
        
#         t=1
#         for i in (data) :
#             if t==1:
#                 print(f"""ID :  name:    age:   marks:
# {i.id}----{i.name}----{i.age}----{i.marks}""")
#             else :
#                 print(f"""{i.id}----{i.name}----{i.age}----{i.marks}""")
#             t+=1

# ### adding prefix to names:  if is_active = 1 add Mr ,and for is_active=0  add Ms

#     @classmethod
#     def add_prefix_to_name(cls):
#         data = cls.objects.filter(is_active=1)
#         for i in data:
#             i.name = "Mr" + i.name
#             i.save()
#         data1 = Student.objects.filter(is_active=0)
#         for j in data1:
#             j.name = "Ms" + j.name
#             j.save()


# ### take  ID number from user  and delete  data for given ID and also return deleted id data

#     @classmethod
#     def delete_id_data(cls):
#         user_input = eval(input("input id number:-"))
#         try:
#             data = cls.objects.get(id = user_input)
#             deleted_item = data.__dict__
#             data.delete() 
#         except Student.DoesNotExist:
#             print("Given ID does not exists")
#         return deleted_item
# ## get count of students whose age is greate than particular value 

#     @classmethod
#     def count_of_student_wrt_age(cls):
#         data = Student.objects.filter(age__gte=25)
#         no_of_student=data.count()
#         return no_of_student,data
        
# ## Get Inactive students :

#     @classmethod
#     def get_inactive_student(cls):  
#         all_inactive_stud = cls.objects.filter(is_active=0)
#         return all_inactive_stud

# ### Insert data from SQL table student2 into model.student ---------------

#     @classmethod
#     def fetch_data_from_sql(cls):
#         data = Student2.objects.all()
#         for i in data:
#             studs = Student(name = i.name,age=i.age,marks = i.marks,is_active=i.is_active)
#             studs.save()

        
# class Student2(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     marks = models.FloatField()
#     is_active = models.BooleanField(default=True)

#     class Meta :
#         db_table = "Student2"
    
#     def __str__(self) :
#         return f"{self.name}"

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     marks = models.FloatField()
#     is_active = models.BooleanField(default=True)

#     department = models.ForeignKey("Department",on_delete=models.SET_NULL,null=True)
    


#     class Meta :
#         db_table = "Stud"
    
#     def __str__(self) :
#         return f"{self.name}"
    
# class College(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)

#     class Meta :
#         db_table = "College"

#     def __str__(self) :
#         return f"{self.name}"

# class Princi(models.Model):
#     name = models.CharField(max_length=100)
#     college = models.OneToOneField(College,on_delete=models.CASCADE,null=True)

#     class Meta:
#         db_table = "princi"

#     def __str__(self) :
#         return f"{self.name}"

# class Department(models.Model):
#     name = models.CharField(max_length=100)
#     college = models.ForeignKey(College,on_delete=models.CASCADE, null = True)
#     intake = models.IntegerField(default=60)

#     class Meta:
#         db_table = "depart"
    
#     def __str__(self) :
#         return f"{self.name}"

    
            

        
        
        


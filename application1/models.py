from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_id=models.IntegerField(null=False)
    employee_img=models.ImageField(upload_to='employee')
    first_name=models.CharField(max_length=100, null=False )
    second_name=models.CharField(max_length=100)
    phone_num=models.IntegerField(null=False)
    email = models.EmailField(null=False)
    salary=models.IntegerField(default=0)
    design=models.CharField(max_length=100, default="Employee")
    def __str__(self):
        return f"{self.employee_id} {self.first_name} {self.second_name} "
    
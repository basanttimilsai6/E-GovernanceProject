from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    permanent_address = models.TextField()
    temporary_address = models.TextField()
    vehicle = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=15)
    license_no = models.CharField(max_length=15)
    issue_date = models.CharField(max_length=50)
    expiry_date = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name
    

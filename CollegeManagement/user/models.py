from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=(('male','male'),('female','female')))
    branch=models.CharField(max_length=50)
    Sid=models.CharField(unique=True)
    date_of_join=models.DateField(auto_now=True)
    year=models.IntegerField()
    semister=models.CharField()
    phone=models.IntegerField(null=True)

    def __str__(self):
        return self.user.get_full_name()

    def set_password(self,raw_password):
        self.password=make_password(raw_password)

    def check_password(self,raw_password):
        return check_password(self.password,raw_password)

class Faculty(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='faculty_profile'
    )
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=(('male','male'),('female','female')))
    branch=models.CharField(max_length=50)
    Fid=models.CharField(unique=True)
    date_of_join=models.DateField(auto_now=True)
    phone=models.IntegerField(null=True)

    def __str__(self):
        return self.user.get_full_name()


    def set_password(self,raw_password):
        self.password=make_password(raw_password)

    def check_password(self,raw_password):
        return check_password(self.password,raw_password)

class Subjects(models.Model):
    user=models.ForeignKey(User,models.CASCADE,related_name='subject')
    name=models.CharField(max_length=30)
    semister=models.IntegerField(default=1,blank=True)
    code=models.CharField(unique=True,max_length=8)
    grade=models.CharField(default='A',max_length=1)

    def __str__(self):
        return self.user.get_full_name()
    

class Marks(models.Model):
    subject=models.ForeignKey(Subjects,models.CASCADE,related_name='marks')
    user=models.ForeignKey(User,models.CASCADE,related_name='user')
    grade=models.CharField(max_length=1,null=True)

    def __str__(self):
        return self.user.get_full_name()

class CGPA(models.Model):
    user=models.ForeignKey(User,models.CASCADE,related_name='cgpa')
    cgpa=models.FloatField(default=5.0)
    isPass=models.BooleanField(default=True)

    def __str__(self):
        return self.cgpa
from .models import Faculty,Student,User,Subjects,Marks
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
     model=User
     fields=['first_name','last_name','email','password','role']
     extra_kwargs = {'password': {'write_only': True}}

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields = [ 'age','branch','gender','Sid','date_of_join',"phone"]

from rest_framework import serializers
from .models import User, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=[
            "age",
            "gender",
            "branch",
            "Sid",
            "semister",
            "year",
            "phone",
        ]

class StudentRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "age",
            "gender",
            "branch",
            "Sid",
            "semister",
            "year",
            "phone",
        ]

    def create(self, validated_data):
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=email,         
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="student",
        )

        student = Student.objects.create(
            user=user,
            **validated_data
        )

        return student

class StudentLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields = [ 'age','branch','gender','Fid','date_of_join','phone']

class FacultyRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Faculty
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "age",
            "gender",
            "branch",
            "Fid",
            "phone",
            # "date_of_join"
        ]

    def create(self, validated_data):
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="faculty",
            is_staff=True,
            
        )

        faculty = Faculty.objects.create(
            user=user,
            **validated_data
        )

        return faculty
class FacultyLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    extra_kwargs = {'password': {'write_only': True}}




from rest_framework import serializers
from .models import Subjects, Marks, CGPA


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'name', 'semister', 'code','grade']


class MarksSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Marks
        fields = ['id', 'subject', 'grade']


class CGPASerializer(serializers.ModelSerializer):
    class Meta:
        model = CGPA
        fields = ['id', 'cgpa', 'isPass']
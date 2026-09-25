from django.contrib.auth import authenticate,login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import StudentLoginSerializer,StudentRegisterSerializer,StudentSerializer,FacultySerializer,FacultyLoginSerializer,FacultyRegisterSerializer,SubjectSerializer,MarksSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Subjects,Marks,User,Student

from rest_framework.permissions import BasePermission

class IsFaculty(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "faculty"
        )

class IsStudent(BasePermission):
    def has_permission(self,request,view):
        return (
            request.user.is_authenticated and request.user.role=='student'
        )

class StudentLogin(APIView):
    def post(self,request):
        serializer=StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            user=authenticate(request,username=email,password=password)

            if user is None:
                return Response({
                    'message':'Invalid Details',
                    'success':False
                },status=status.HTTP_400_BAD_REQUEST)
            login(request,user)
            refresh=RefreshToken.for_user(user)
            if user.role!='student':
                return Response({
                        'message':'User is not a student',
                        'success':False
                    },status=status.HTTP_400_BAD_REQUEST)

            student=user.student_profile


            return Response(
                {
                    "success": True,
                    "message": "Login Successful",
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": student.age,
                    "gender": student.gender,
                    "branch": student.branch,
                    "Sid": student.Sid,
                    "role": user.role,
                    "phone":student.phone
                },
                status=status.HTTP_200_OK,
            )
        return Response({
            'message':'Invalid email or password',
            'success':False

        },status=status.HTTP_400_BAD_REQUEST)

class StudentRegister(APIView):
    permission_classes=[IsFaculty]
    def post(self,request):
        serializer=StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    
                    'message':"registration successfull",
                    'success':True
                },status=status.HTTP_200_OK
            )
        return Response(
                        {
                            'errors':serializer.errors,
                            'message':"Invalid details",
                            'success':False
                        },status=status.HTTP_400_BAD_REQUEST
                    )

class FacultyLogin(APIView):
    def post(self,request):
        serializer=FacultyLoginSerializer(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                refresh=RefreshToken.for_user(user)
                if user.role!='faculty':
                    return Response({
                            'message':'User is not a student',
                            'success':False
                        },status=status.HTTP_400_BAD_REQUEST)
    
                faculty=user.faculty_profile
    
    
                return Response(
                    {
                        "success": True,
                        "message": "Login Successful",
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "age": faculty.age,
                        "gender": faculty.gender,
                        "branch": faculty.branch,
                        "Fid": faculty.Fid,
                        "role": user.role,
                        "phone":faculty.phone
                    },
                    status=status.HTTP_200_OK,
                )
                

            return Response(
                    {
                        'message':"Invalid details",
                        'success':False
        
                    },status=status.HTTP_400_BAD_REQUEST
                )


        return Response(
            {
                'message':"Invalid details",
                'success':False

            },status=status.HTTP_400_BAD_REQUEST
        )

class FacultyRegister(APIView):
    
    def post(self,request):
        serializer=FacultyRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message':"registration successfull",
                    'success':True
                },status=status.HTTP_200_OK
            )
        return Response(
                        {
                            'errors':serializer.errors,
                            'message':"Invalid details",
                            'success':False
                        },status=status.HTTP_400_BAD_REQUEST
                    )

class Profile(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        if user.role=='student':
            student=user.student_profile
            return Response(
                {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": student.age,
                    "gender": student.gender,
                    "branch": student.branch,
                    "Sid": student.Sid,
                    "role": user.role,
                    "year":student.year,
                    "semister":student.semister,
                    "phone":student.phone
                },
                status=status.HTTP_200_OK,
            )
        if user.role=='faculty':
            faculty=user.faculty
            return Response(
                {
                    
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": faculty.age,
                    "gender": faculty.gender,
                    "branch": faculty.branch,
                    "Fid": faculty.Fid,
                    "role": user.role,
                    "phone":faculty.phone
                },
                status=status.HTTP_200_OK,
            )
        return Response({
            'message':'Invalid email or password',
            'success':False

        },status=status.HTTP_400_BAD_REQUEST)

class StudentMarks(APIView):
    permission_classes=[IsStudent]
    def get(self,request):
        user=request.user
        try:
            if user.role=='student':
                

                subjects=Subjects.objects.filter(user=user)
                serializer=SubjectSerializer(subjects,many=True)

                return Response(
                    {
                        'name':f"{user.first_name} {user.last_name}",
                        'marks':serializer.data
                    }
                )
        except:
            return Response({
                "message":'Invalid access',
                'success':False
            },status=status.HTTP_400_BAD_REQUEST)
        

class StudentAcademicDetails(APIView):
    permission_classes=[IsFaculty]
    def get(self,request,pk):
        try:
            user=User.objects.get(id=pk)
            # student=user.student
            subjects=Subjects.objects.filter(user=user)
            serializer=SubjectSerializer(subjects,many=True)
            # marks=Marks.objects.filter(user=user)
            # serializer=MarksSerializer(marks,many=True)
            return Response(
                {
                    'success':True,
                    'marks':serializer.data,
                },status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({

                'success':False,
                'message':str(e)
            },status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
            data=request.data
            subject,created=Subjects.objects.get_or_create(user=user,name=data['name'],semister=data['semister'],code=data['code'],grade=data['grade'])
            subject.save()
            
            return Response(
                {
                    'message':'Posted successfully',
                    'success':True,
                    'marks': SubjectSerializer(subject).data
                }
            )
        except Exception as e:
            return Response(
                {
                    'errors':str(e),
                    'message':'Invalid Details',
                    'success':False
                },status=status.HTTP_400_BAD_REQUEST
            )


    
    def put(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
            data=request.data
            subject=Subjects.objects.get(user=user,name=data['name'])
            subject.grade=data['grade']
            # marks=Marks.objects.get(user=user,subject=subject)
            # marks.grade=data['grade']
            # marks.save()
            return Response(
                {
                    "success": True,
                    "message": "Marks updated successfully."
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                'errors':str(e),
                'success':False,
                'message':"Invalid details"
            },status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            user=User.objects.get(pk=pk)
            subject=subject.objects.get(user=user,name=request.data['name'])
            # marks=Marks.objects.get(user=user,subject=subject)
            if subject:
                subject.delete()
                return Response({
                    'message':'Deleted Successfully',
                    'success':True
                },status=status.HTTP_200_OK)
            else:
                return Response(
                {
                    'message':"Not Found",
                    'success':False
                },status=status.HTTP_400_BAD_REQUEST
            )
        except Exception:
            return Response(
                {
                    'message':"Not Found",
                    'success':False
                },status=status.HTTP_400_BAD_REQUEST
            )

class UpdateStudentDetails(APIView):
    permission_classes=[IsFaculty]

    def get(self,request,pk):
        user=get_object_or_404(User,pk)
        if user is None:
            return Response({
                'message':'Invalid Details',
                'success':False
            },status=status.HTTP_400_BAD_REQUEST)
        if user.role!='student':
            return Response({
                'message':'User is not a student',
                'success':False
            },status=status.HTTP_400_BAD_REQUEST)
    
        student=user.student_profile
        return Response(
                    {
                        "success": True,
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "age": student.age,
                        "gender": student.gender,
                        "branch": student.branch,
                        "Sid": student.Sid,
                        "role": user.role,
                        "phone":student.phone
                    },
                    status=status.HTTP_200_OK,
                )
    def put(self,request,pk):
        user=get_object_or_404(User,pk)
        try:
            student=Student.objects.get(user=user)
            user.first_name = request.data.get("first_name", user.first_name)
            user.last_name = request.data.get("last_name", user.last_name)
            user.email = request.data.get("email", user.email)
            user.save()

            # Update Student fields
            student.roll_no = request.data.get("roll_no", student.roll_no)
            student.branch = request.data.get("branch", student.branch)
            student.year = request.data.get("year", student.year)
            student.phone = request.data.get("phone", student.phone)
            student.save()

            return Response(
                {
                    "success": True,
                    "message": "Student details updated successfully"
                }
            )
        except Exception:
            return Response(
                {
                    "message":"Invalid data",
                    'success':False,
                },status=status.HTTP_400_BAD_REQUEST
            )
    def delete(self,request,pk):
        try:
            user=get_object_or_404(User,pk)
            if user:
                user.delete()
                return Response(
                    {
                        "message":"Student deleted successfully",
                        'success':True
                    },status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'message':"Student not found",
                        'success':True
                    },status=status.HTTP_400_BAD_REQUEST
                )
        except Exception:
                return Response(
                    {
                        "message":"Invalid data",
                        'success':False,
                    },status=status.HTTP_400_BAD_REQUEST
                )

class StudentList(APIView):
    permission_classes=[IsFaculty]

    def get(self,request):
        students=Student.objects.all()
        data=[]
        for student in students:
            data.append({
                'id':student.user.id,
                'name':f"{student.user.first_name} {student.user.last_name}",
                'sid':student.sid,
                'branch':student.branch,
                'gender':student.gender
            })
        return Response({
            'data':data,
            'success':True

        },status=status.HTTP_200_OK)
    
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


# Creating view using 'ViewSet'
class StudentViewSet(viewsets.ViewSet):

    # this method return list of record from database
    def list(self, request):
        print("*********List********")
        print("Basename: ", self.basename)  # 'student'
        print("Action: ", self.action)  # 'list'
        print("Detail: ", self.detail)  # 'False'
        print("Suffix: ", self.suffix)  # 'List'
        print("Name: ", self.name)  # 'None'
        print("Description: ", self.description)  # 'None'
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    # This method will return one record according to given 'pk'
    def retrieve(self, request, pk=None):
        print("*********Retrieve********")
        print("Basename: ", self.basename)  # 'student'
        print("Action: ", self.action)  # 'retrieve'
        print("Detail: ", self.detail)  # 'True'
        print("Suffix: ", self.suffix)  # 'Instance'
        print("Name: ", self.name)  # 'None'
        print("Description: ", self.description)  # 'None'
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    # This method will create a new object and save into database
    def create(self, request):
        print("*********Create********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This method will complete update the record in the database
    def update(self, request, pk):
        print("*********Update********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # This method will partial update the record in the database
    def partial_update(self, request, pk):
        print("*********Partial Update********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors)

    # This method will delete the record from the database
    def destroy(self, request, pk):
        print("*********Destroy********")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        id = pk
        Student.objects.get(id=id).delete()
        return Response({'msg': "Data deleted"})

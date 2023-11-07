from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
 

class StudentDetail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if request.method=='GET':
            if pk is None:
                user = Student.objects.all()
                serializer = StudentSerializer(user, many=True)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                id = Student.objects.filter(pk=pk).first()
                if id is not None:
                    serializer = StudentSerializer(id)
                    return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'msg':'user not found'},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, pk=None):
        # user = request.data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        id = Student.objects.filter(pk=pk).first()
        serializer = StudentSerializer(id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':serializer.data},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        id = Student.objects.filter(pk=pk).first()
        serializer = StudentSerializer(id, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        id = Student.objects.filter(pk=pk).first()
        if id is not None:
            id.delete()
            return Response({'msg':'Data deleted'},status=status.HTTP_200_OK)
        return Response({'msg':'user not found'},status=status.HTTP_400_BAD_REQUEST)
# class StudentDetail_2(APIView):
#     pass
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializers
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class StudentDetail(APIView):

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        if request.method == "GET":
            details= Student.objects.all()
            serializer = StudentSerializers(details, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request, fromat=None):
        if request.method == "POST":
            serializer = StudentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetail1(APIView):

    def get(self, request, pk):

        if request.method == 'GET':
            id = Student.objects.get(pk=pk)
            
            serializers = StudentSerializers(id)
            return Response(serializers.data,status=status.HTTP_200_OK)

    def put(self, request, pk, fromat=None):
        if request.method=="PUT":
            id = Student.objects.get(pk=pk)
            serializer = StudentSerializers(id, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        if request.method=="DELETE":
            id = Student.objects.get(pk=pk)
            # serializer = StudentSerializers(id, data=request.data)
            id.delete()
            return Response({'msg':'deleted'},status=status.HTTP_200_OK)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view, APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
class ContactView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        query = Contact.objects.all()
        serializer = ContactSerializer(query, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self, request, id):
        query = Contact.objects.get(id=id)
        serializer = ContactSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id):
        query = Contact.objects.get(id=id)
        query.delete()
        return Response("Record has been deleted successfully!!")
    


@api_view(["POST"])
def logout(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
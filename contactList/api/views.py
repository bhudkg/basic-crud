from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def contact_view(request):
    query = Contact.objects.all()
    serializer = ContactSerializer(query, many=True)
    if request.method == "GET":
        return Response(serializer.data)

@api_view(['POST'])
def update_contact_view(request):
    serializer = ContactSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def modify_contact(request, pk):
    query = Contact.objects.filter(id=pk)
    serializer = ContactSerializer(query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


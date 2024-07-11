from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view, APIView
from .serializers import *
from rest_framework.response import Response
# Create your views here.

# @api_view(['GET'])
# def contact_view(request):
#     query = Contact.objects.all()
#     serializer = ContactSerializer(query, many=True)
#     if request.method == "GET":
#         return Response(serializer.data)

# @api_view(['POST'])
# def update_contact_view(request):
#     serializer = ContactSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
    
# @api_view(['PUT'])
# def modify_contact(request, id):
#     query = Contact.objects.get(id=id)
#     serializer = ContactSerializer(query, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)

# @api_view(['DELETE'])
# def delete_contact(request, id):
#     query = Contact.objects.get(id=id)
#     query.delete()
#     return Response("message: Record has been deleted.")


class ContactView(APIView):
    
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


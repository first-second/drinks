#from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.views import ObtainAuthToken
from getpass import getpass
import requests
import os

class CustomAuthToken(ObtainAuthToken):
    pass

@api_view(['GET','POST'])
def drink_list(request):
    url = 'http://127.0.0.1:8000/api-token-auth/'
    username=input("enter username : ")
    password=getpass("enter password : ")
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    response_data=response.json()
    token=response_data['token']
    headers = {'Authorization': 'Token ' + token}
    if request.method == 'GET':
        drinks=Drink.objects.all()
        serializer=DrinkSerializer(drinks,many=True)
        return Response(serializer.data,headers=headers)
    
    if request.method == 'POST':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)

@api_view(['GET','PUT','DELETE'])
def drink_details(request,id):
    url = 'http://127.0.0.1:8000/api-token-auth/'
    username=input("enter username : ")
    password=getpass("enter password : ")
    data = {'username': username, 'password': password}
    response = requests.post(url, data=data)
    response_data=response.json()
    token=response_data['token']
    headers = {'Authorization': 'Token ' + token}
    try:
        drink=Drink.objects.get(pk=id)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=DrinkSerializer(drink)
        return Response(serializer.data,headers=headers)
    #put is to update data already in database
    elif request.method == 'PUT':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)
    elif request.method == "DELETE":
        if drink.delete():
            return HttpResponse("Deleted successfully",status=204)
        else:
            return HttpResponse("invalid data",status=405)

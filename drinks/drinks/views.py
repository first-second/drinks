#from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken

class CustomAuthToken(ObtainAuthToken):
    pass



@api_view(['GET','POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks=Drink.objects.all()
        serializer=DrinkSerializer(drinks,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_details(request,id):
    try:
        drink=Drink.objects.get(pk=id)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=DrinkSerializer(drink)
        return Response(serializer.data)
    #put is to update data already in database
    elif request.method == 'PUT':
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method("DELETE"):
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

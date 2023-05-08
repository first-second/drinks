#from django.http import JsonResponse
from drinks.models import Drink
from drinks.serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.views import ObtainAuthToken
import requests

API_KEY="ee976b9f40b84b11af9136c525cc5618"

class CustomAuthToken(ObtainAuthToken):
    pass


def home(request):
    '''
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = 'https://newsapi.org/v2/top-headlines?country='+str(country)+'&apiKey='+API_KEY
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = 'https://newsapi.org/v2/top-headlines?category='+str(category)+'&apiKey='+API_KEY
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        '''
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey='+API_KEY
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'articles' : articles
    }

    return render(request, './home.html', context)

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
    elif request.method == "DELETE":
        if drink.delete():
            return HttpResponse("Deleted successfully",status=204)
        else:
            return HttpResponse("invalid data",status=405)

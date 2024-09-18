import requests
from django.shortcuts import render


def home(request):
  response = requests.get('https://dog.ceo/api/breeds/image/random')
  data = response.json()
  result = data['message']
  return render(request, 'templates/index.html',{'result': result})
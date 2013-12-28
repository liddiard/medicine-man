from django.shortcuts import render
from .models import Domain
# Create your views here.

def route (request):
    url = request.META['HTTP_HOST']
    print url
    domain =Domain.objects.get(url = 'url')
    print domain.kind

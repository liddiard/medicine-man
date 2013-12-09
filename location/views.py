from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class FrontView(TemplateView):

    template_name = "location/front.html"

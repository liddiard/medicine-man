from django.shortcuts import render
from django.views.generic import TemplateView


class FrontView(TemplateView):

    template_name = "location/front.html"

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Site, Image


class FrontView(TemplateView):

    template_name = "content/front.html"

    def get_context_data(self, **kwargs):
        context = super(FrontView, self).get_context_data(**kwargs)
        domain = self.kwargs['domain']
        context['site'] = Site.objects.get(domain=domain)
        return context

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Site, Artwork


class FrontView(TemplateView):

    template_name = "location/front.html"

    def get_context_data(self, **kwargs):
        context = super(FrontView, self).get_context_data(**kwargs)
        domain = self.kwargs['domain']
        context['site'] = Site.objects.get(domain=domain)
        context['gallery'] = Artwork.objects.order_by('?')
        return context

from django.http import HttpResponse
from django.views.generic import TemplateView

from router.models import Domain
from .models import Site, Image


class FrontView(TemplateView):

    template_name = "content/front.html"

    def get(self, request, **kwargs):
        domain = self.kwargs['domain']
        context = self.get_context_data()
        try:
            context['site'] = Site.objects.get(domain=domain)
        except Site.DoesNotExist:
            domain_name = Domain.objects.get(id=domain)
            return self.site_dne_error(domain_name)
        return self.render_to_response(context)

    def site_dne_error(self, domain_name):
        error_msg = '''
            A content Site object matching this domain does not exist. If 
            you're the administrator of this site, you can fix this by adding 
            a content Site with "%s" as the domain.
        '''
        return HttpResponse(error_msg % domain_name, content_type='text/plain')

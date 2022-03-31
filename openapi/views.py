from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView


class SwaggerUIView(TemplateView):
    '''
    Shows interactive OpenAPI docs in Swagger UI
    '''
    template_name = 'swagger-ui.html'

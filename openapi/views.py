from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


@method_decorator(login_required(), name='dispatch')
class SwaggerUIView(TemplateView):
    """
    View that presets the OpenAPI docs in Swagger UI
    """
    template_name = 'swagger-ui.html'
    extra_context = {'schema_url': 'openapi:schema'}
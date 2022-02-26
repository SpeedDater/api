from django.conf import settings
from django.views.generic.base import TemplateView


class SwaggerUIView(TemplateView):
    """
    View that presets the OpenAPI docs in Swagger UI
    """
    template_name = 'swagger-ui.html'
    extra_context = {'APP_NAME': settings.APP_NAME,
                     'schema_url': 'openapi:schema'}

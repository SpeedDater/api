from django.conf import settings


# global site information
def global_tags(request):
    context = {
        'APP_NAME': settings.APP_NAME,
    }
    return context

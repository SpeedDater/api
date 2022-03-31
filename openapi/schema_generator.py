from django.template.loader import render_to_string
from django.urls import reverse
from rest_framework.schemas.openapi import SchemaGenerator


class SpeedDaterSchemaGenerator(SchemaGenerator):
    '''
    Generate standard OpenAPI schema with Bearer authentication and some extra info
    '''

    def get_schema(self, *args, **kwargs):
        '''
        Overrides the built-in get_schema() method to inject extra info
        '''
        schema = super().get_schema(*args, **kwargs)

        # add API description from swagger-ui-description.md template
        content_rendered = render_to_string('swagger-ui-description.md')
        # haxx to convert to normal str: concat rendered template with empty str
        # wtf why is there no way to convert from a django.utils.safestring.SafeString to str
        schema['info']['description'] = content_rendered + ''

        # add license info
        schema['info']['license'] = {
            'name': 'GNU AGPLv3',
            'url': 'https://www.gnu.org/licenses/agpl-3.0-standalone.html',
        }
        # add authentication spec
        schema['components']['securitySchemes'] = {
            'APIToken': {
                'type': 'http',
                'description': 'Provide your API Token here.',
                'scheme': 'Bearer',
            }
        }
        # require token authentication globally
        schema['security'] = [
            {'APIToken': []},
        ]
        # overwrite security for auth endpoints
        schema['paths'][reverse('rest_login')]['post']['security'] = []
        schema['paths'][reverse('rest_login_google')]['post']['security'] = []
        # remove GET for logout endpoint (shouldn't even exist in the first place)
        schema['paths'][reverse('rest_logout')].pop('get')

        return schema

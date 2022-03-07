from django.conf import settings
from django.urls import reverse
from rest_framework.schemas.openapi import SchemaGenerator


class SpeedDaterSchemaGenerator(SchemaGenerator):
    '''
    Generate standard OpenAPI schema with Bearer authentication and some extra info
    '''

    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        # add more info about the API
        schema['info']['description'] = settings.APP_DESCRIPTION
        schema['info']['license'] = {
            'name': 'GNU AGPLv3',
            'url': 'https://www.gnu.org/licenses/agpl-3.0-standalone.html',
        }
        # add authentication spec
        schema['components']['securitySchemes'] = {
            'API Token': {
                'type': 'http',
                'description': '''
**[Generate API Token]()**  
You may authenticate against the API with an API Token.  
Provide the token in the `Authorization` header in this format:  
`Authorization: Bearer <token>`
				''',
                'scheme': 'Bearer',
            }
        }
        schema['security'] = [
            {'API Token': []},
        ]
        # overwrite security for auth endpoints
        schema['paths'][reverse('rest_login')]['post']['security'] = []
        schema['paths'][reverse('rest_login_google')]['post']['security'] = []
        # remove GET for logout endpoint (shouldn't even exist)
        schema['paths'][reverse('rest_logout')].pop('get')
        return schema

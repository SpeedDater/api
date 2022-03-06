from rest_framework.schemas.openapi import SchemaGenerator


class SpeedDaterSchemaGenerator(SchemaGenerator):
    """
    A standard OpenAPI schema with Bearer authentication added
    """

    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        # add more info about the API
        schema["info"]["description"] = "This is the REST API for the SpeedDater service."
        schema["info"]["license"] = {
            "name": "GNU AGPLv3",
            "url": "https://www.gnu.org/licenses/agpl-3.0-standalone.html",
        }
        # add authentication spec
        schema["components"]["securitySchemes"] = {
            "API Token": {
                "type": "http",
                "description": """
**[Generate API Token]()**  
You may authenticate against the API with an API Token.  
Provide the token in the `Authorization` header in this format:  
`Authorization: Bearer <token>`
				""",
                "scheme": "Bearer",
            }
        }
        schema["security"] = [
            {"API Token": []},
        ]
        # overwrite security for auth endpoints
        schema["paths"]["/rest-auth/login/"]["post"]["security"] = []
        schema["paths"]["/rest-auth/google/login/"]["post"]["security"] = []
        return schema

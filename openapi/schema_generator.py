from rest_framework.schemas.openapi import SchemaGenerator


class SpeedDaterSchemaGenerator(SchemaGenerator):
	"""
	A standard OpenAPI schema with Bearer authentication added
	"""
	def get_schema(self, *args, **kwargs):
		schema = super().get_schema(*args, **kwargs)
		schema["components"]["securitySchemes"] = {
			"Bearer": {
				"type": "http",
				"scheme": "bearer"
			}
		}
		schema["security"] = [
			{"Bearer": []},
		]
		return schema

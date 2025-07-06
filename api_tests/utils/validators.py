import jsonschema
from jsonschema import validate
import json
import os

# Загрузка схем из api.json
with open("api.json", "r") as f:
    openapi_spec = json.load(f)

def validate_json(instance, schema_key):
    """Валидация JSON по схеме из api.json"""
    schema = openapi_spec["components"]["schemas"][schema_key]
    try:
        validate(instance=instance, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise AssertionError(f"JSON не соответствует схеме {schema_key}: {e}")
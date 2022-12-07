import functools

from flask import request
from werkzeug.exceptions import BadRequest


class datarequired:
    def __init__(self, schema):
        self.schema = schema

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(*args, **kwargs):

            setattr(request, "params_schema", {})

            for k in self.schema.keys():

                key_format, key_required = self.schema[k]
                data_value = request.json.get(k)

                if key_required and data_value is None:
                    raise BadRequest(f"Invalid schema, {k} is required")

                if data_value is None:
                    continue

                try:
                    request.params_schema[k] = key_format(data_value)
                except Exception as e:
                    raise BadRequest(f"Invalid schema {e}")

            return view(*args, **kwargs)

        return wrapper

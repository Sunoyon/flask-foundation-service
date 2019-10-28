from flask_rebar import RequestSchema
from marshmallow import fields


class BookRequestSchema(RequestSchema):
    name = fields.String(required=True)

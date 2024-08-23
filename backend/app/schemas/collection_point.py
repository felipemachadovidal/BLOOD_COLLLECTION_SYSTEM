from marshmallow import Schema, fields

class CollectionPointSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    user_id = fields.Int(required=True)


from flask_restx import Model, fields

StackModel = Model('StackModel', {
    "id": fields.Integer(required=True, description="Id of the stack"),
    "elements": fields.List(
        fields.Float,
        required=True,
        description="Elements of the stack"
    ),
})

ElementInput = Model('ElementInput', {
    "element": fields.Float(
        required=True,
        description="New element to push in the stack"
    ),
})

ErrorReponse = Model('ErrorReponse', {
    'success': fields.Boolean(required=True),
    'error': fields.String(required=True),
})

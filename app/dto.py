
from flask_restx import Model, fields

# Dto for Stack
StackModelDto = Model('StackModelDto', {
    "id": fields.Integer(required=True, description="Id of the stack"),
    "elements": fields.List(
        fields.Float,
        required=True,
        description="Elements of the stack"
    ),
    'created_at': fields.DateTime(required=True),
})

# Dto for pushing new element into a stack
ElementInputDto = Model('ElementInputDto', {
    "element": fields.Float(
        required=True,
        description="New element to push in the stack"
    ),
})

# Dto for structured error response
ErrorReponseDto = Model('ErrorReponseDto', {
    'success': fields.Boolean(required=True),
    'error': fields.String(required=True),
})

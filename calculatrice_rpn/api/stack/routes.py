from flask_restx import Namespace, Resource, cors
from calculatrice_rpn.dao import stacks
from .dtos import StackModel, ErrorReponse, ElementInput

api = Namespace(
    'Stack',
    path='/rpn/stack',
    decorators=[cors.crossdomain(origin="*")]
)

api.models[StackModel.name] = StackModel
api.models[ErrorReponse.name] = ErrorReponse
api.models[ElementInput.name] = ElementInput


@api.route("")
class StackListResource(Resource):
    """Resource for stack list management"""

    @api.response(201, 'Created', model=StackModel)
    def post(self):
        """Create a new stack"""
        return stacks.create(), 201

    @api.response(200, 'Ok', model=[StackModel])
    def get(self):
        """List the available stacks"""
        return stacks.stacks, 200


@api.route('/<int:stack_id>')
@api.param('stack_id', 'Stack identifier')
class StackResource(Resource):
    """Resource for handling a stack"""

    @api.expect(ElementInput)
    @api.response(200, 'Ok', model=StackModel)
    @api.response(404, "Not found", model=ErrorReponse)
    def post(self, stack_id):
        """Push a new value to a stack"""
        updated_stack = stacks.push_element(stack_id, api.payload["element"])
        if updated_stack:
            return updated_stack, 200
        return {'success': False, 'error': 'Stack not found'}, 404

    @api.response(200, 'Ok', model=StackModel)
    @api.response(404, "Not found", model=ErrorReponse)
    def get(self, stack_id):
        """Get a stack"""
        existing_stack = stacks.get(stack_id)
        if existing_stack:
            return existing_stack, 200
        return {'success': False, 'error': 'Stack not found'}, 404

    @api.response(204, "No Content")
    def delete(self, stack_id):
        """Delete a stack"""
        return stacks.delete(stack_id), 204

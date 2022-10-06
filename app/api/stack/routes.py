"""Routes definition for stack."""
from flask_restx import Namespace, Resource, cors, marshal
from app.db import stack_repository
from app.dto import ElementInputDto, ErrorReponseDto, StackModelDto

# Create a new API namespace
api = Namespace(
    'Stack',
    path='/rpn/stack',
    decorators=[cors.crossdomain(origin="*")]
)

# Inject required dto into the namespace
api.models[StackModelDto.name] = StackModelDto
api.models[ErrorReponseDto.name] = ErrorReponseDto
api.models[ElementInputDto.name] = ElementInputDto


@api.route("")
class StackListResource(Resource):
    """Resource for stack list management"""

    @api.marshal_with(StackModelDto, code=201, description='Created')
    def post(self):
        """Create a new stack"""
        return stack_repository.create(), 201

    @api.marshal_list_with(StackModelDto, code=200, description='Ok')
    def get(self):
        """List the available stacks"""
        return stack_repository.stacks, 200


@api.route('/<int:stack_id>')
@api.param('stack_id', 'Stack identifier')
class StackResource(Resource):
    """Resource for handling a stack"""

    @api.expect(ElementInputDto)
    @api.response(200, "Ok", model=StackModelDto)
    @api.response(404, "Not found", model=ErrorReponseDto)
    def post(self, stack_id):
        """Push a new value to a stack"""
        updated_stack = stack_repository.push_element(stack_id, api.payload["element"])
        if updated_stack:
            return marshal(updated_stack, StackModelDto), 200
        return marshal({'success': False, 'error': 'Stack not found'}, ErrorReponseDto), 404

    @api.response(200, "Ok", model=StackModelDto)
    @api.response(404, "Not found", model=ErrorReponseDto)
    def get(self, stack_id):
        """Get a stack"""
        existing_stack = stack_repository.get(stack_id)
        if existing_stack:
            return marshal(existing_stack, StackModelDto), 200
        return marshal({'success': False, 'error': 'Stack not found'}, ErrorReponseDto), 404

    @api.response(204, "No Content")
    def delete(self, stack_id):
        """Delete a stack"""
        return stack_repository.delete(stack_id), 204

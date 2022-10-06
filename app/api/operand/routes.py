"""Routes definition for operand."""
from flask_restx import Namespace, Resource, cors, marshal
from app.config import Config
from app.dto import StackModelDto, ErrorReponseDto
from app.db import stack_repository

# Create a new API namespace
api = Namespace(
    'Operation',
    path='/rpn/op',
    decorators=[cors.crossdomain(origin="*")]
)

# Inject required dto into the namespace
api.models[StackModelDto.name] = StackModelDto
api.models[ErrorReponseDto.name] = ErrorReponseDto

@api.route("")
class OperandResource(Resource):
    """Resource for operand"""

    @api.response(200, 'Ok', model=[str])
    def get(self):
        """List all the operand"""
        return Config.OPERAND_LIST, 200


@api.route('/<string:op>/stack/<int:stack_id>')
@api.param('op', 'Operand',  enum=['+', '-', '*', 'div'])
@api.param('stack_id', 'Stack identifier')
class StackOperationResource(Resource):
    """Stack operation"""

    @api.response(200, 'Ok', model=StackModelDto)
    @api.response(404, "Not found", model=ErrorReponseDto)
    def get(self, op, stack_id):
        """Apply an operand to a stack"""

        # Check if op is a valid and supported operand
        if op not in Config.OPERAND_LIST:
            return {'success': False, 'error': 'Operand not found'}, 404
        try:
            # Try run the calculation
            updated_stack = stack_repository.apply_operand(op, stack_id)
            if updated_stack:
                return marshal(updated_stack, StackModelDto), 200
            return marshal({'success': False, 'error': 'Stack not found'}, StackModelDto), 404
        except Exception as err:
            return marshal({'success': False, 'error': f'{err}'}, ErrorReponseDto), 404

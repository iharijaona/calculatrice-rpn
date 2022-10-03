from flask_restx import Namespace, Resource, cors
from calculatrice_rpn.config import Config
from calculatrice_rpn.api.stack.dtos import StackModel, ErrorReponse
from calculatrice_rpn.dao import stacks

api = Namespace(
    'Operation',
    path='/rpn/op',
    decorators=[cors.crossdomain(origin="*")]
)

api.models[StackModel.name] = StackModel
api.models[ErrorReponse.name] = ErrorReponse

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

    @api.response(200, 'Ok', model=StackModel)
    @api.response(404, "Not found", model=ErrorReponse)
    def get(self, op, stack_id):
        """Apply an operand to a stack"""

        if op not in Config.OPERAND_LIST:
            return {'success': False, 'error': 'Operand not found'}, 404

        try:
            updated_stack = stacks.apply_operand(op, stack_id)
            if updated_stack:
                return updated_stack
            return {'success': False, 'error': 'Stack not found'}, 404
        except Exception as err:
            return {'success': False, 'error': f'{err}'}, 404

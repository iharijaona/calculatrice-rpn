OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "div": lambda x, y: x / y
}


class StackDAO(object):
    def __init__(self):
        self.counter = 0
        self.stacks = []

    def get(self, stack_id):
        found_stacks = [*filter(lambda elem: elem['id'] == stack_id, self.stacks)]
        if len(found_stacks):
            return found_stacks[0]

    def create(self):
        self.counter += 1
        new_stack = {
            'id': self.counter,
            'elements': [],
        }
        self.stacks.append(new_stack)
        return new_stack

    def push_element(self, stack_id, element):
        existing_stack = self.get(stack_id)
        if existing_stack:
            existing_stack['elements'].append(element)
            return existing_stack

    def apply_operand(self, op, stack_id):
        existing_stack = self.get(stack_id)
        if existing_stack:
            try:
                elements_remaining = existing_stack['elements'][:-2]
                elements_for_calc = existing_stack['elements'][-2:]
                existing_stack['elements'] = elements_remaining + \
                                             [self.__compute(op, elements_for_calc[0], elements_for_calc[1])]
                return existing_stack
            except Exception as err:
                raise RuntimeError('Calculation failed: impossible to apply the operand!')

    def delete(self, stack_id):
        existing_stack = self.get(stack_id)
        if existing_stack:
            self.stacks.remove(existing_stack)

    def __compute(self, op, element_x, element_y):
        return OPERATIONS.get(op)(element_x, element_y)

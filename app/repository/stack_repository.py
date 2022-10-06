from app.model import StackModel 

#: Implementation of all supported operation
OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "div": lambda x, y: x / y
}


class StackRepository:
    """Static repository for the Stack."""

    def __init__(self):
        self.clear_all()

    def get(self, stack_id) -> StackModel | None:
        """Find a stack by id"""
        found_stacks = [*filter(lambda elem: elem.id == stack_id, self.stacks)]
        if len(found_stacks):
            return found_stacks[0]

    def create(self) -> StackModel:
        """Create a new empty stack"""
        # Increment the counter (simulate auto-increment id)
        self.counter += 1

        # Create a dict for the new stack
        new_stack =  StackModel(self.counter)
        
        # Add the new element to the list of stack
        self.stacks.append(new_stack)

        # Return the newly created stack
        return new_stack

    def push_element(self, stack_id, element) -> StackModel | None:
        """Push a new element in the specified stack"""
        # Find the specified stack by id
        existing_stack = self.get(stack_id)
        if existing_stack:
            # Add the new element to the end of the existing
            # elements of the specified stack.
            existing_stack.elements.append(element)
            # Return the updated stack
            return existing_stack

    def apply_operand(self, op, stack_id) -> StackModel | None:
        """Run calculation by applying the given operand on the specified stack"""
        # Find the specified stack by id
        existing_stack = self.get(stack_id)
        if existing_stack:
            try:
                # Extract the last two elements for the calculation
                elements_for_calc = existing_stack.elements[-2:]
                # Apply the operand and rebuild the elements
                existing_stack.elements = \
                    existing_stack.elements[:-2] + [
                        self.__compute(op, elements_for_calc[0],
                                       elements_for_calc[1])
                    ]
                # Return the updated stack
                return existing_stack
            except Exception as err:
                raise RuntimeError('Calculation failed: impossible to apply the operand!')

    def delete(self, stack_id):
        """Remove a stack by id"""
        # Find the specified stack by id
        existing_stack = self.get(stack_id)
        if existing_stack:
            # Remove the stack from the list
            self.stacks.remove(existing_stack)

    def __compute(self, op, element_x, element_y):
        """Apply an operand on two elements x,y"""
        return OPERATIONS.get(op)(element_x, element_y)
    
    def clear_all(self):
        self.counter = 0
        self.stacks: StackModel = []

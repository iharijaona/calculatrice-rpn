from flask_testing import TestCase
from app.db import stack_repository
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        stack_repository.clear_all()
        
    def test_find_all_operand(self):
        """Try to Find all the operand"""
        response = self.client.get("/rpn/op")
        operands = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(operands, list)
        self.assertEqual(len(operands), 4)
        
    
    def test_calculation_with_addition_operand(self):
        """Try applying calculation"""
        stack = stack_repository.create()
        self.client.post(f'/rpn/stack/{stack.id}', json={
            'element': 10
        })
        self.client.post(f'/rpn/stack/{stack.id}', json={
            'element': 5
        })
        self.client.post(f'/rpn/stack/{stack.id}', json={
            'element': 6
        })
        
        response = self.client.get(f'/rpn/op/+/stack/{stack.id}')

        returned_stack = response.json
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(returned_stack['elements'], list)
        self.assertEqual(len(returned_stack['elements']), 2)
        self.assertEqual(returned_stack['elements'][0], 10)
        self.assertEqual(returned_stack['elements'][1], 11)
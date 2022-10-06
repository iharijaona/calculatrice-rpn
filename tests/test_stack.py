from flask_testing import TestCase
from wsgi import app
from app.db import stack_repository

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        stack_repository.clear_all()
        
    def test_create_empty_stack(self):
        """Try to a new empty stack"""
        response = self.client.post('/rpn/stack')
        stack = response.json
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(stack, dict)
        self.assertIsInstance(stack['id'], int)
        self.assertIsInstance(stack['elements'], list)
        self.assertEqual(len(stack['elements']), 0)
    
    def test_find_all_stack(self):
        """Try find all stack"""
        response = self.client.get(f'/rpn/stack')
        returned_stacks_before = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(returned_stacks_before, list)
        self.assertEqual(len(returned_stacks_before), 0)
        
        # Add two stack
        stack_repository.create()
        stack_repository.create()
        
        # Find and check if the two stacks are returned
        response = self.client.get(f'/rpn/stack')
        returned_stacks_after = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(returned_stacks_after, list)
        self.assertEqual(len(returned_stacks_after), 2)
        
    def test_create_new_stack_then_try_to_find_it_by_id(self):
        """Try find a stack by id"""
        stack = stack_repository.create()
        response = self.client.get(f'/rpn/stack/{stack.id}')
        returned_stack = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(returned_stack, dict)
        self.assertEqual(stack.id, returned_stack['id'])
        
    def test_find_non_existing_stack_should_raise_error(self):
        """Check if the attempt to find a non-existent stack returns an error."""
        response = self.client.get(f'/rpn/stack/999')
        error_response = response.json
        self.assertEqual(response.status_code, 404)
        self.assertEqual(error_response['success'], False)
        
    def test_delete_existing_stack(self):
        """Delete existing stack."""
        stack = stack_repository.create()
        response = self.client.delete(f'/rpn/stack/{stack.id}')
        self.assertEqual(response.status_code, 204)
        
    def test_push_element_into_a_stack(self):
        """Try to push an elemet into a stack."""
        stack = stack_repository.create()
        self.client.post(f'/rpn/stack/{stack.id}', json={
            'element': 1
        })
        self.client.post(f'/rpn/stack/{stack.id}', json={
            'element': 2
        })
        response = self.client.post(f'/rpn/stack/{stack.id}', json={
            'element': 3
        })
        returned_stack = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(returned_stack['elements'], list)
        self.assertEqual(len(returned_stack['elements']), 3)

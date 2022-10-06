# pylint: disable=missing-docstring
from datetime import datetime


class StackModel:
    """Data model for the stack"""
    
    def __init__(self, id):
        self.id = id
        self.elements = []
        self.created_at = datetime.now()
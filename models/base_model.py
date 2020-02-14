#!/usr/bin/python3

""" Import Modules to get Time and ID generators """
from datetime import datetime
from uuid import uuid4 as uuid


class BaseModel:
    """ BaseModel Creator Structure. """

    def __init__(self):
        """ BaseModel instance initialization. """
        self.id = str(uuid())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

# Modify Instances

    def save(self):
        """ Save changes of a BaseModel instances. """
        self.updated_at = datetime.now()

# Get info of instance

    def to_dict(self):
        """ Return all info of a BaseModel instance. """
        return {**self.__dict__, '__class__': self.getType,
                'updated_at': str(self.updated_at),
                'created_at': str(self.created_at)}

# Print info of instances

    @property
    def getType(self):
        """ retrieves self type """
        return self.__class__.__name__

    def f(self, string):
        """ sumulate f-strings available from python 3.6 """
        return string.format(**locals())

    def __str__(self):
        """ Prints info of a BaseModel instance. """
        return self.f('[{self.getType}] ({self.id}) {self.__dict__}')

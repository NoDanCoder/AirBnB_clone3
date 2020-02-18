#!/usr/bin/python3
""" Module to add City Class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class structure (city info) """
    state_id = ""
    name = ""

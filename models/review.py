#!/usr/bin/python3
""" Module to add Review Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class structure (review info) """
    place_id = ""
    user_id = ""
    text = ""

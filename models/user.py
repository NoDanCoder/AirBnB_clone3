#!/usr/bin/python3
""" Module to add User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class structure (user personal info) """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3

""" create the unique instance to operate JSON files """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

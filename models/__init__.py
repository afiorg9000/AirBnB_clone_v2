#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    import FileStorage
    storage = FileStorage()
    storage.reload()

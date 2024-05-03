#!/usr/bin/python3
"""
initialize the models package
"""
from models.engine import file_storage

classes = file_storage.FileStorage.classes
storage = file_storage.FileStorage()
storage.reload()

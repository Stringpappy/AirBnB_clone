#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""

from .file_storage import FileStorage

"""variable storage that stand as an instance of filestorage"""
storage = FileStorage()

"""reload"""
storage.reload()

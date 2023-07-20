#!/usr/bin/python3
""" This module defines the Base super class """
import json


class Base:
    """
    This is the base (super) class for all other classes
    in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor of the Base class which
        initializes its public instance id property
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        a static method that converts a list of dictionaries
        to its JSON string representation and returns it if it
        exists else returns an empty string.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """  """
        if json_string is None:
            return []
        dicts_list = json.loads(json_string)
        return dicts_list

    @classmethod
    def save_to_file(cls, list_objs):
        """
        serializes the list of base objects to a file in their JSON
        format if they exist else serializes an empty list.
        """
        filename = cls.__name__ + ".json"
        arr = []

        if list_objs is not None:
            for obj in list_objs:
                arr.append(obj.to_dictionary())

        _json = cls.to_json_string(arr)
        with open(filename, 'w') as f:
            f.write(_json)

    @classmethod
    def create(cls, **dictionary):
        """
        create a new base sub class whose properties are updated
        with the dictionary argument property
        """
        if cls.__name__ is 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ is 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ deserializes persisted properties back to base sub instances"""
        list_of_base_objs = []

        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                buffer = f.read()
        except FileNotFoundError:
            return []

        list_of_dictionaries = cls.from_json_string(buffer)

        for dictionary in list_of_dictionaries:
            list_of_base_objs.append(cls.create(**dictionary))

        return list_of_base_objs

#!/usr/bin/python3

import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        arr = []

        for obj in list_objs:
            arr.append(obj.to_dictionary())
        _json = cls.to_json_string(arr)

        with open(filename, 'w') as f:
            f.write(_json)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

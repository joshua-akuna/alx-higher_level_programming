#!/usr/bin/python3
""" This module defines the Base super class """
import json
import csv


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
        """converts a json string to a base object dictionary"""
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
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes a list of Base sub classes to a csv file"""
        filename = cls.__name__ + '.csv'

        if list_objs is not None:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)

                for obj in list_objs:
                    writer.writerow([repr(obj)])

    @classmethod
    def load_from_file_csv(cls):
        """
        reads data from a csv file and converts each row to
        a base object.
        """
        list_of_base_objs = []
        filename = cls.__name__ + '.csv'

        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                rows = [cls.csv_row_to_base_obj(row[0]) for row in reader]
        except FileNotFoundError:
            return []
        return rows

    @classmethod
    def csv_row_to_base_obj(cls, csv_row):
        """This method converts a single csv row to a base object"""
        params = csv_row.split(',')

        if (len(params) == 4):
            _dict = {
                'id': int(params[0]),
                'size': int(params[1]),
                'x': int(params[2]),
                'y': int(params[3])
            }
        elif (len(params) == 5):
            _dict = {
                'id': int(params[0]),
                'width': int(params[1]),
                'height': int(params[2]),
                'x': int(params[3]),
                'y': int(params[4])
            }
        base_obj = cls.create(**_dict)
        return base_obj

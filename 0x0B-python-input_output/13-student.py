#!/usr/bin/python3


class Student():
    """A student class
    """

    def __init__(self, first_name, last_name, age):
        """initializes Student

        Attributes:
            self.first_name: first name of a student
            self.last_name: last name of a student
            self.age: age of a student

        Args:
            first_name: first name of a student
            last_name: last name of a student
            age: age of a student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure
           for JSON serialization of Student

        Returns:
            dict: the dictionary

        """
        if attrs:
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json (dict): dictionary of attributes read from json file

        """
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            elif key == "last_name":
                self.last_name = json[key]
            elif key == "age":
                self.age = int(json[key])

#!/usr/bin/python3
'''
Defines unittests for Base Class
'''
import unittest
import json
import sys
import os
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):
    '''Testing Base class'''

    @classmethod
    def setUpClass(cls):
        '''Test Instances'''
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(12)
        cls.b4 = Base()
        cls.r1 = Rectangle(3, 5, 1, id=9)
        cls.r3 = Rectangle(2, 4, id=11)
        cls.s1 = Square(5, id=99)
        cls.s2 = Square(7, 9, 1, id=78)

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4

    def test_base_class_docstring(self):
        self.assertIsNotNone(Base.__doc__)

    def test_base_init(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
        self.assertEqual(self.b4.id, 3)

    def test_base_init_docstring(self):
        self.assertIsNotNone(Base.__init__.__doc__)

    def test_base_to_json_string_docstring(self):
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_base_from_json_string_docstring(self):
        self.assertIsNotNone(Base.from_json_string.__doc__)

    def test_base_create_docstring(self):
        self.assertIsNotNone(Base.create.__doc__)

    def test_base_save_to_file_docstring(self):
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_base_load_from_file_docstring(self):
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def checking(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(save_to_file.__doc__)
        self.assertIsNotNone(from_json_string.__doc__)
        self.assertIsNotNone(create.__doc__)
        self.assertIsNotNone(load_from_file.__doc__)

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    def test_to_json_string_AND_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_create(self):
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertEqual(r2.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertFalse(self.r1 is r2)
        self.assertFalse(self.r1 == r2)

    def test_save_to_file_AND_load_from_file(self):
        list_rectangles_input = [self.r1, self.r3]

        Rectangle.save_to_file(list_rectangles_input)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        with open('Rectangle.json', 'r') as f:
            r_total = sum(1 for _ in f)
        self.assertGreater(r_total, 0)
        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        list_squares_input = [self.s1, self.s2]

        Square.save_to_file(list_squares_input)
        self.assertTrue(os.path.isfile('Square.json'))

        with open('Square.json', 'r') as f:
            s_total = sum(1 for _ in f)
        self.assertGreater(s_total, 0)
        list_squares_output = Square.load_from_file()

        for square in list_squares_input:
            self.assertIsInstance(square, Square)

        for square in list_squares_output:
            self.assertIsInstance(square, Square)

        Base._Base__nb_objects -= 4

    def test_empty(self):
        """Test to check from empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_None(self):
        """
        Test to check from none empty
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
'''
Defines unittest for Square class
'''
import unittest
import sys
import os
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareClass(unittest.TestCase):
    '''Testing Square class'''

    @classmethod
    def setUpClass(cls):
        '''Testing Instances'''
        Base._Base__nb_objects = 0
        cls.s1 = Square(5)
        cls.s2 = Square(2, 2)
        cls.s3 = Square(3, 1, 3)

    @classmethod
    def tearDownClass(cls):
        '''Removing Testing Instances'''
        pass

    def test_square_class_docstring(self):
        self.assertIsNotNone(Square.__doc__)

    def test_square_str_docstring(self):
        self.assertIsNotNone(Square.__str__.__doc__)

    def test_square_init_docstring(self):
        self.assertIsNotNone(Square.__init__.__doc__)

    def test_square_update_docstring(self):
        self.assertIsNotNone(Square.update.__doc__)

    def test_square_to_dictionary_docstring(self):
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_square_str(self):
        self.assertEqual(str(self.s1), '[Square] (1) 0/0 - 5')
        self.assertEqual(str(self.s2), '[Square] (2) 2/0 - 2')
        self.assertEqual(str(self.s3), '[Square] (3) 1/3 - 3')

    def test_square_area(self):
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 9)

    def test_square_size(self):
        self.assertEqual(self.s1.size, self.s1.height, self.s1.width)
        self.assertEqual(self.s2.size, self.s2.height, self.s2.width)
        self.assertEqual(self.s3.size, self.s3.height, self.s3.width)

    def test_square_negative_size_init(self):
        self.assertRaises(ValueError, Square, -1)

    def test_square_wrong_size_type_init(self):
        self.assertRaises(TypeError, Square, '10')

    def test_square_negative_x_or_y(self):
        self.assertRaises(ValueError, Square, 5, -1, 0)
        self.assertRaises(ValueError, Square, 5, 0, -12)

    def test_square_wrong_type_x_or_y(self):
        self.assertRaises(TypeError, Square, [5, '12', 0])
        self.assertRaises(TypeError, Square, [5, -1, []])

    def test_square_update(self):
        self.s1.update(1, 2, 3, 4)
        self.assertEqual(str(self.s1), '[Square] (1) 3/4 - 2')
        self.s1.update(x=12)
        self.assertEqual(str(self.s1), '[Square] (1) 12/4 - 2')
        self.s1.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s1), '[Square] (89) 12/1 - 7')

    def test_square_update_too_many_arguments(self):
        s5 = Square(5, id=10)
        s5.update(7, 8, 5, 5, 10, 14, 18, 20)
        self.assertEqual(str(s5), '[Square] (7) 5/5 - 8')

    def test_square_update_add_new_key(self):
        s5 = Square(5, id=10)
        s5.update(id=7, size=5, x=2, y=2, blah=25)
        self.assertNotIn('area', s5.__dict__)

    def test_square_update_with_negative_values(self):
        self.assertRaises(ValueError, self.s2.update, 10, -1, 3)
        self.assertRaises(ValueError, self.s2.update, 10, 1, -5)

    def test_square_update_with_wrong_value_type(self):
        self.assertRaises(TypeError, self.s2.update, 10, 1, [])
        self.assertRaises(TypeError, self.s2.update, 10, [], 3)

    def test_square_to_dictionary(self):
        self.assertDictEqual(self.s3.to_dictionary(),{'size': 3, 'x': 1, 'y': 3, 'id': 3} )

    def test_square_dictionary_to_json(self):
        dictionary = self.s3.to_dictionary()
        self.assertIsInstance(Base.to_json_string(dictionary), str)

    def test_square_save_to_file(self):
        sq1 = Square(5)
        sq2 = Square(15)
        Square.save_to_file([sq1, sq2])
        self.assertTrue(os.path.isfile('Square.json'))
        with open('Square.json') as f:
            num_lines = sum(1 for line in f)
        self.assertGreater(num_lines, 0)

    def test_square_display(self):
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        s5 = Square(4)
        s5.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n####\n####\n")


if __name__ == '__main__':
    unittest.main()
    

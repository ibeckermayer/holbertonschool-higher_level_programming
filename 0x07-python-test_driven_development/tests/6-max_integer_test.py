import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_Integer(unittest.TestCase):
    """Test the max_integer function from 6-max_integer.py
    """

    def test_empty(self):
        """Test that the max of an empty list
        """
        result = max_integer([])
        self.assertIsNone(result)

    def test_int_err(self):
        """Testing without a list
        """
        self.assertRaises(TypeError, lambda: max_integer(1))

    def test_len_1_1(self):
        """Test for list with length 1
        """
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_len_1_2(self):
        """Test for list with length 1
        """
        result = max_integer([-1])
        self.assertEqual(result, -1)

    def test_len_2_2(self):
        """test lists of ints with length 2
        """
        result = max_integer([1, 1])
        self.assertEqual(result, 1)

    def test_len_2_3(self):
        """test lists of ints with length 2
        """
        result = max_integer([-1, -1])
        self.assertEqual(result, -1)

    def test_len_2_4(self):
        """test lists of ints with length 2
        """
        result = max_integer([-1, 1])
        self.assertEqual(result, 1)

    def test_len_2_5(self):
        """test lists of ints with length 2
        """
        result = max_integer([1, -1])
        self.assertEqual(result, 1)

    def test_len_3_1(self):
        """test lists of ints with length 3
        """
        result = max_integer([1, 1, 1])
        self.assertEqual(result, 1)

    def test_len_3_2(self):
        """test lists of ints with length 3
        """
        result = max_integer([-1, -1, -1])
        self.assertEqual(result, -1)

    def test_len_3_3(self):
        """test lists of ints with length 3
        """
        result = max_integer([-1, 0, 1])
        self.assertEqual(result, 1)

    def test_len_3_4(self):
        """test lists of ints with length 3
        """
        result = max_integer([1, 0, -1])
        self.assertEqual(result, 1)

    def test_list_of_list_1(self):
        """Test a list of lists
        """
        result = max_integer([[1], [1], [1]])
        self.assertEqual(result, [1])

    def test_list_of_list_2(self):
        """Test a list of lists
        """
        result = max_integer([[1], [3], [2]])
        self.assertEqual(result, [3])

    def test_list_of_list_3(self):
        """Test a list of lists
        """
        result = max_integer([[1, 1000], [3], [2, 1000]])
        self.assertEqual(result, [3])

    def test_list_of_list_4(self):
        """Test a list of lists
        """
        result = max_integer([[1, 1000], [2, 100], [2, 1000]])
        self.assertEqual(result, [2, 1000])

    def test_list_of_list_5(self):
        """Test a list of lists
        """
        result = max_integer([[1000, 0], [2, 10000], [3, 10000]])
        self.assertEqual(result, [1000, 0])

    def test_list_of_list_6(self):
        """Test a list of lists
        """
        result = max_integer([[[12, 12], 11], [[12, 11], [12, 40]]])
        self.assertEqual(result, [[12, 12], 11])

    def test_list_of_list_err(self):
        """Test a list of lists
        """
        self.assertRaises(TypeError,
                          lambda: max_integer([
                                  [[12, 11], 11],
                                  [[12, 11], [12, 40]]
                          ]))

    def test_with_bool_1(self):
        """Test using booleans
        """
        result = max_integer([False, True])
        self.assertEqual(result, True)

    def test_with_bool_2(self):
        """Test using booleans
        """
        result = max_integer([False, True, 1])
        self.assertEqual(result, True)

    def test_with_bool_3(self):
        """Test using booleans
        """
        result = max_integer([False, 1, True])
        self.assertEqual(result, 1)

    def test_with_bool_4(self):
        """Test using booleans
        """
        result = max_integer([False, -1, 0])
        self.assertEqual(result, False)

    def test_with_bool_5(self):
        """Test using booleans
        """
        result = max_integer([0, -1, False])
        self.assertEqual(result, 0)

    def test_with_str_1(self):
        """Testing using strings
        """
        result = max_integer(["a", "z"])
        self.assertEqual(result, 'z')

    def test_with_str_2(self):
        """Testing using strings
        """
        result = max_integer(["az"])
        self.assertEqual(result, 'az')

    def test_with_str_3(self):
        """Testing using strings
        """
        result = max_integer(["az", "by"])
        self.assertEqual(result, 'by')

    def test_with_str_4(self):
        """Testing using strings
        """
        result = max_integer(["az", "ay"])
        self.assertEqual(result, 'az')

    def test_with_str_err(self):
        """Testing using strings
        """
        self.assertRaises(TypeError, lambda: max_integer(["z", 100]))

    def test_with_dic(self):
        """Testing using a dictionary with sequential keys starting at 0
        """
        result = max_integer({0:100, 1:2, 2:3})
        self.assertEqual(result, 100)

    def test_with_dic_err(self):
        """Test when keys aren't sequential starting at 0
        """
        self.assertRaises(KeyError, lambda: max_integer({0:100, 4:3, 3:4}))

    def test_with_empty_set(self):
        """Test with an empty set
        """
        result = None
        self.assertIsNone(result)

    def test_with_set(self):
        """Test with a set with some integers in it
        """
        self.assertRaises(TypeError, lambda: max_integer({1, 2, 3}))


if __name__ == '__main__':
    unittest.main()

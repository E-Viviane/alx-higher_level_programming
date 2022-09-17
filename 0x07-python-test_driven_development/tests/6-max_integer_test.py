nteger_test.py

"""Unittests for max_integer([..])."""



import unittest

max_integer = __import__('6-max_integer').max_integer





class TestMaxInteger(unittest.TestCase):

        """Define unittests for max_integer([..])."""



            def test_ordered_list(self):

                        """Test an ordered list of integers."""

                                ordered = [1, 2, 3, 4]

                                        self.assertEqual(max_integer(ordered), 4)



                                            def test_unordered_list(self):

                                                        """Test an unordered list of integers."""

                                                                unordered = [1, 2, 4, 3]

                                                                        self.assertEqual(max_integer(unordered), 4)



                                                                            def test_max_at_begginning(self):

                                                                                        """Test a list with a beginning max value."""

                                                                                                max_at_beginning = [4, 3, 2, 1]

                                                                                                        self.assertEqual(max_integer(max_at_beginning), 4)



                                                                                                            def test_empty_list(self):

                                                                                                                        """Test an empty list."""

                                                                                                                                empty = []

                                                                                                                                        self.assertEqual(max_integer(empty), None)



                                                                                                                                            def test_one_element_list(self):

                                                                                                                                                        """Test a list with a single element."""

                                                                                                                                                                one_element = [7]

                                                                                                                                                                        self.assertEqual(max_integer(one_element), 7)



                                                                                                                                                                            def test_floats(self):

                                                                                                                                                                                        """Test a list of floats."""

                                                                                                                                                                                                floats = [1.53, 6.33, -9.123, 15.2, 6.0]


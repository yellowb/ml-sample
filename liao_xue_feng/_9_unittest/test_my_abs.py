# Unittest sample of my_abs


import unittest

from liao_xue_feng._9_unittest.my_abs import my_abs


class TestMyAbs(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(my_abs(9), 9, 'positive number test failed.')

    def test_negative_number(self):
        self.assertEqual(my_abs(-9), 9, 'negative number test failed.')

    def test_zero_number(self):
        self.assertEqual(my_abs(0), 0, 'zero number test failed.')

    def test_not_number(self):
        self.assertRaises(TypeError)

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

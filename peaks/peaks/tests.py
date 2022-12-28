from django.test import TestCase
import unittest

class PeakClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)



    def check_if_user_name_is_string(self):
        print("Method: check_if_user_name_is_string")
        self.assertEqual("username", str)

from django.test import TestCase
import unittest

# class CalcTests ( unittest.TestCase ):
#     def test_add ( self ):
#         self .assertEqual(calc.add( 1 , 2 ), 3 )
#     def test_sub ( self ):
#         self .assertEqual(calc.sub( 4 , 2 ), 2 )

# if _name__ == '__main__' :
# unittest.main()


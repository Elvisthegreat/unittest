import unittest
from evens import even_number_of_evens # importing our function from evens.py

class TestEvens(unittest.TestCase):

   def test_throws_error_if_value_passed_in_is_not_list(self):
      """
      raise a TypeError if the value pass into
      the function is not list
      """
      self.assertRaises(TypeError, even_number_of_evens, 4)

if __name__ == 'main':
   unittest.main()
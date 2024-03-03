import unittest
from evens import even_number_of_evens # importing our function from evens.py

class TestEvens(unittest.TestCase):

   def test_throws_error_if_value_passed_in_is_not_list(self):
      """
      raise a TypeError if the value pass into
      the function is not list
      """
      self.assertRaises(TypeError, even_number_of_evens, 4)
   

   def test_values_in_list(self):
   
      self.assertEqual(even_number_of_evens([]), False) # returns False if an empty list is passed in
      self.assertEqual(even_number_of_evens([2, 4]), True) # return True if two even number are pass into it
      self.assertEqual(even_number_of_evens([2]), False) # fail if only one even number is passed in
      self.assertEqual(even_number_of_evens([1, 3, 5]), False) # fail if odd number is pass in has a list

if __name__ == 'main':
   unittest.main()
"""Unit Testing"""
# -------------------------------------------------------------
# Test Runner:
# -the module that run the unit testing (pytest, unittest)
# -------------------------------------------------------------
# Test Case
# - smallest unit of testing
# - it use assert methods to check for actions and responses
# Test Suite 
# - collection of mutiple tests or test cases
# Test Report
# - a full report contains the failure or succeed
# -------------------------------------------------------------
# unittest
# - add tests into classes as methods
# - use a series of special assertion methods
# -------------------------------------------------------------

import unittest

# assert 3*8 == 23, "should be 24"

# ""REPRESENT CUSTOM REPORT <you write it by yourself>""
# def test_case_one():

#     assert 5 * 10 == 50,"should be 50"

# def test_case_two():

#     assert 5 * 50 == 240,"should be 250"    

# if __name__ == "__main__":

#     test_case_one()
#     test_case_two()

#     print("All Tests Passed")    
# -------------------------------------------------------------

class MyTestCase(unittest.TestCase):

    def test_one(self):

        self.assertTrue(100 > 92, "Should Be True")

    def test_two(self):

        self.assertEqual(40 * 10, 400, "Sould Be 400")    

    def test_three(self):

        self.assertGreater(100, 101, "Should Be True")    

if __name__ == "__main__":

    unittest.main()        
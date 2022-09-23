#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest
# inherit the TestCase class
class TestRearrange(unittest.TestCase):
    # ready to write first test case
    def test_basic(self):
        # we setting up our expected inputs and outputs
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        # assertEqual to verify what we expected is exactly what we got

    # we test empty string
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    # In this case, we're testing that someone with more than one given name still gets their name properly rearranged, Let's test it! 
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

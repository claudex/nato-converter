#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nato_converter
import unittest

class TestFindInTable(unittest.TestCase):
    def test_find_lower(self):
        self.assertEqual("alpha", nato_converter.find_in_table("a"))

    def test_find_upper(self):
        self.assertEqual("ALPHA", nato_converter.find_in_table("A"))

    def test_find_space(self):
        self.assertEqual("", nato_converter.find_in_table(" "))
        self.assertEqual("", nato_converter.find_in_table("\t"))
        self.assertEqual("", nato_converter.find_in_table("\n"))
       
    def test_find_multiple(self):
        self.assertRaises(nato_converter.IllegalStringSize,
                nato_converter.find_in_table, "aa")

    def test_find_digit(self):
        self.assertEqual("Unaone", nato_converter.find_in_table("1"))

    def test_find_special_char(self):
        self.assertEqual(u"é", nato_converter.find_in_table(u"é"))

if __name__ == '__main__':
    unittest.main()

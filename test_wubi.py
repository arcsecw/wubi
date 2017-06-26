# -*- coding: utf-8 -*-

import unittest

import wubi
from wubi._compat import u


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_chinese2wubi(self):
        self.assertEqual(wubi.get('王文超，爱自由。\n\t你好','cw'),u('gggg yygy fhv , ep thd mh . \n\t wq vb'))
    def test_wubi2chinese(self):
        self.assertEqual(wubi.get('gggg yygy fhv , ep thd mh . \n\t wq vb','wc'),u('王文超，爱自由。\n\t你好'))

if __name__ == '__main__':
    unittest.main()

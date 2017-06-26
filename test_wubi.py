# -*- coding: utf-8 -*-

import unittest

import wubi
from wubi._compat import u


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def test_chinese_with_english1(self):
        self.assertEqual(wubi.get('Wen Chao Wang 爱自由','cw'),'WenChaoWang ep thd mh')
    def test_chinese_with_english2(self):
        self.assertEqual(wubi.get('WenChao Wang 爱自由','cw'),'WenChaoWang ep thd mh')
    def test_chinese_with_english3(self):
        self.assertEqual(wubi.get('WenChaoWang 爱自由','cw'),'WenChaoWang ep thd mh')

    def test_wibi_with_english1(self):
        self.assertEqual(wubi.get('WenChaoWang ep thd mh','wc'),u('WenChaoWang爱自由'))
    def test_wubi_with_english2(self):
        self.assertEqual(wubi.get('WenChaoWang ep thd mh','wc'),u('WenChaoWang爱自由'))
    def test_wubi_with_english3(self):
        self.assertEqual(wubi.get('WenChaoWang ep thd mh','wc'),u('WenChaoWang爱自由'))




if __name__ == '__main__':
    unittest.main()

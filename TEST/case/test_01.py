#coding: utf-8

import unittest

class aaa(unittest.TestCase):
    '''加减运算接口测试'''
    @classmethod
    def setUpClass(cls):
        print("zhi gao yi ci ")
    @classmethod
    def tearDownClass(cls):
        print("2222")
    def setUp(self):
        self.a=1

    def tearDown(self):
        print("qingkong")
    def testAdd(self):
        '''加法运算'''
        # a = 1
        b = 2
        self.assertEqual(3,self.a)

    def testJian(self):

        c =3
        self.assertTrue(c-self.a == 1)
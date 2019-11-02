import unittest
import random

# each assignment will be checked as std1
# don't change this line
from std1 import * 

class unit_test(unittest.TestCase):

    def test_SumEven_1(self):
        self.assertTrue(SumEven([1,2,3,4])==6)
        self.assertTrue(SumEven([2,4])==6)
        self.assertTrue(SumEven([1,2,3,4])==6)
        self.assertTrue(SumEven([-2,2])==0)

    def test_sharpsearch_a_3(self):
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        s = SharpSearch(data)
        self.assertIsInstance(s, SharpSearch)

    def test_sharpsearch_b_4(self):
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        s = SharpSearch(data)
        self.assertTrue(s.SearchFirst(4)==2)
        self.assertTrue(s.SearchFirst(9)==6)
        self.assertTrue(s.SearchFirst(4)==2)
        
    def test_sharpsearch_c_5(self):
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        s = SharpSearch(data)
        self.assertTrue(s.SearchLast(9)==6)
        self.assertTrue(s.SearchLast(12)==11)
        self.assertTrue(s.SearchLast(4)==9)
        self.assertTrue(s.SearchLast(9)==6)

    def test_sharpsearch_d_6(self):
        # case 1
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        s = SharpSearch(data)
        self.assertTrue(s.Search(4)==2)
        self.assertTrue(s.Search(4)==7)
        self.assertTrue(s.Search(4)==9)
        self.assertTrue(s.Search(4)==-1)

        # case 2
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        s = SharpSearch(data)
        self.assertTrue(s.Search(11)==10)
        self.assertTrue(s.Search(11)==-1)

        # case 3
        data = [1,3,4,5,7,3,9,4,5,4,11,12]
        s = SharpSearch(data)
        self.assertTrue(s.Search(111)==-1)
        self.assertTrue(s.Search(111)==-1)

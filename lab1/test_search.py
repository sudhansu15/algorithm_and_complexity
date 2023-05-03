import unittest
from search import linear_search
from search import binary_search
class SearchTestCase(unittest.TestCase):
    """test for linear_search.py"""
    def test_linear_search(self):
        """Does linear search algorithm work correctly"""
        values = [5,3,6,1,4,9,0]
        self.assertEqual(linear_search(values,5),0)
        self.assertEqual(linear_search(values,1),3)
        self.assertEqual(linear_search(values,10),-1)
    

    def test_binary_search(self):
        """Does binary search algorithm work correctly"""
        # def binary_search(arr, low, high, target):
        arr = [1,3,6,8,11,23,56,83]
        self.assertEqual(binary_search(arr,0,7,11),4)
        self.assertEqual(binary_search(arr,0,7,56),6)
        self.assertEqual(binary_search(arr,0,7,99),-1)




if __name__ =='__main__':
    unittest.main()



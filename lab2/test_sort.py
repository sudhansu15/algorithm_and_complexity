import unittest
from sort import InsertionSort , MergeSort

class   SortTestCase(unittest.TestCase):
    def test_Insertion_Sort(self):
        values = [5,2,4,7,1,3,8,6]
        input1 = [8,66,54,32,69,21,420,5,13]
        self.assertEqual(InsertionSort(values),[1,2,3,4,5,6,7,8])
        self.assertEqual(InsertionSort(input1),[5,8,13,21,32,54,66,69,420])


    # TO BE NOTED: infinite value for this code is 100000001. i.e, the test case will run for array having value <=100000000
    def test_Merge_Sort(self):
        values = [46,24,12,88,29,53,18,36]
        input1 = [8,66,54,32,69,21,20,5,13]
        self.assertEqual(MergeSort([5,2,4,7,1,3,8,6],0,7),[1,2,3,4,5,6,7,8])
        self.assertEqual(MergeSort(input1,0,8),[5,8,13,20,21,32,54,66,69])
        # the output of the insertionsort can be used as test condition for an array
        self.assertEqual(MergeSort(values,0,7),InsertionSort(values)) 



if __name__ =='__main__':
    unittest.main()
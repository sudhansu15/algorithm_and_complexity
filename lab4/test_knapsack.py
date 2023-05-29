import unittest
from knapsack import Brute_Force_01Knapsack
from knapsack import Brute_Force_fractionalKnapsack
from knapsack import Greedy_fractionalKnapsack

class KnapsackTestCase(unittest.TestCase):
    
    def test_Brute_Force_01Knapsack(self):
        p = [60,100,120]
        w = [10,20,30]
        m = 55
        input = Brute_Force_01Knapsack(p,w,m)
        output = ('011',220)
        self.assertEqual(input, output)


        p = [20, 30, 40, 50, 60]
        w = [10, 20, 30, 40, 50]
        m = 100
        input = Brute_Force_01Knapsack(p,w,m)
        output = ('11110', 140)
        self.assertEqual(input, output)

    def test_Brute_Force_fractionalKnapsack(self):
        p = [60,100,120]
        w = [10,20,30]
        m = 55
        input = Brute_Force_fractionalKnapsack(p,w,m)
        output = 260.0
        self.assertEqual(input, output)

        p = [20, 30, 40, 50, 60]
        w = [10, 20, 30, 40, 50]
        m = 100
        input = Brute_Force_fractionalKnapsack(p,w,m)
        output = 140
        self.assertEqual(input, output)
    

    def test_Greedy_fractionalKnapsack(self):
        p = [60,100,120]
        w = [10,20,30]
        m = 55
        input = Greedy_fractionalKnapsack(p,w,m)
        output = 260.0
        self.assertEqual(input, output)


        p = [20, 30, 40, 50, 60]
        w = [10, 20, 30, 40, 50]
        m = 100
        input = Greedy_fractionalKnapsack(p,w,m)
        output = 140
        self.assertEqual(input, output)
    


if __name__ == "__main__":
    unittest.main()    
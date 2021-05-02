import unittest
import sorters.bubbleSort


class TestBubbleSort(unittest.TestCase):
    # Test an unsorted list of numbers
    def test_sortAll(self):
        org_data = [9, 1, 4, 6, 7, -2, 0, 13, 11, 15]
        exp_data = [-2, 0, 1, 4, 6, 7, 9, 11, 13, 15]
        sorters.bubbleSort.bubbleSort(org_data)
        self.assertEqual(org_data, exp_data)

    # Test an already sorted list of numbers
    def test_alreadySorted(self):
        org_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        exp_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sorters.bubbleSort.bubbleSort(org_data)
        self.assertEqual(org_data, exp_data)

    def test_reverseSort(self):
        org_data = [5, 4, 3, 2, 1]
        exp_data = [1, 2, 3, 4, 5]
        sorters.bubbleSort.bubbleSort(org_data)
        self.assertEqual(org_data, exp_data)


if __name__ == '__main__':
    unittest.main()

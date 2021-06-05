import unittest
import sorters.insertionSort


class TestInsertionSort(unittest.TestCase):
    # Test an unsorted list of numbers
    def test_sortAll(self):
        org_data = [9, 1, 54, -2, 8, 23]
        exp_data = [-2, 1, 8, 9, 23, 54]
        sorters.insertionSort.insertionSort(org_data)
        self.assertEqual(org_data, exp_data)

    # Test an already sorted list of numbers
    def test_alreadySorted(self):
        org_data = [5, 10, 15, 20, 25, 30]
        exp_data = [5, 10, 15, 20, 25, 30]
        sorters.insertionSort.insertionSort(org_data)
        self.assertEqual(org_data, exp_data)

    # Test an unsorted list of numbers that needs to get reversed to be sorted
    def test_reverseSort(self):
        org_data = [-5, -10, -15, -20, -25]
        exp_data = [-25, -20, -15, -10, -5]
        sorters.insertionSort.insertionSort(org_data)
        self.assertEqual(org_data, exp_data)


if __name__ == '__main__':
    unittest.main()

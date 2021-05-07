import unittest
import sorters.quickSort


class TestQuickSort(unittest.TestCase):
    # Test an unsorted list of numbers
    def test_sortAll(self):
        org_data = [-4, 2, 18, 1, 0, 4, 100]
        exp_data = [-4, 0, 1, 2, 4, 18, 100]
        sorters.quickSort.quickSort(org_data, 0, len(org_data)-1)
        self.assertEqual(org_data, exp_data)

    # Test an already sorted list of numbers
    def test_alreadySorted(self):
        org_data = [10, 20, 30, 40, 50]
        exp_data = [10, 20, 30, 40, 50]
        sorters.quickSort.quickSort(org_data, 0, len(org_data)-1)
        self.assertEqual(org_data, exp_data)

    # Test an unsorted list of numbers that needs to get reversed to be sorted
    def test_reverseSort(self):
        org_data = [5, 4, 3, 2, 1]
        exp_data = [1, 2, 3, 4, 5]
        sorters.quickSort.quickSort(org_data, 0, len(org_data)-1)
        self.assertEqual(org_data, exp_data)


if __name__ == '__main__':
    unittest.main()

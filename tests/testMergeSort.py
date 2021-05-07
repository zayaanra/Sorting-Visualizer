import unittest
import sorters.mergeSort


class TestMergeSort(unittest.TestCase):
    # Test an unsorted list of numbers
    def test_sortAll(self):
        org_data = [-4, 21, 2, 1, 17, 3, 0, -12]
        exp_data = [-12, -4, 0, 1, 2, 3, 17, 21]
        ret = sorters.mergeSort.mergeSort(org_data)
        self.assertEqual(ret, exp_data)

    # Test an already sorted list of numbers
    def test_alreadySorted(self):
        org_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        exp_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        ret = sorters.mergeSort.mergeSort(org_data)
        self.assertEqual(ret, exp_data)

    # Test an unsorted list of numbers that needs to get reversed to be sorted
    def test_reverseSort(self):
        org_data = [5, 4, 3, 2, 1]
        exp_data = [1, 2, 3, 4, 5]
        ret = sorters.mergeSort.mergeSort(org_data)
        self.assertEqual(ret, exp_data)


if __name__ == '__main__':
    unittest.main()

import unittest
from arknights_recurit import ArkHeadhunt

class MyTestCase(unittest.TestCase):

    def test_one_pull_without_offset(self):
        base = ArkHeadhunt(times=1)
        base.get_randomized_results(0)
        class_list = base.random_class
        self.assertEqual(len(class_list), 1)

    def test_one_pull_with_offset_guarantee(self):
        base = ArkHeadhunt(times=1)
        base.get_randomized_results(98)
        class_list = base.random_class
        self.assertListEqual(class_list, [6])

    def test_ten_pull_without_offset(self):
        base = ArkHeadhunt(times=10)
        base.get_randomized_results(0)
        class_list = base.random_class
        self.assertEqual(len(class_list), 10)

    def test_edge_case_0_pulls(self):
        base = ArkHeadhunt(times=0)
        base.get_randomized_results(0)
        class_list = base.random_class
        self.assertEqual(len(class_list), 0)

    def test_edge_case_negative_pulls(self):
        base = ArkHeadhunt(-1)
        self.assertRaises(ValueError, base.get_randomized_results, 0)

    def test_ten_pull_with_offset(self):
        base = ArkHeadhunt(times=10)
        base.get_randomized_results(98)
        class_list = base.random_class
        full_10_list = [6] * 10
        self.assertListEqual(class_list, full_10_list)



if __name__ == '__main__':
    unittest.main()

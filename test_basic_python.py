import unittest
from basic_python import count_fragment_combinations

class TestCountFragmentCombinations(unittest.TestCase):
    def test_example_from_docstring(self):
        fragments = [1, 23, 4]
        message = 1234
        self.assertEqual(count_fragment_combinations(fragments, message), 1)

    def test_multiple_ways(self):
        fragments = [12, 3, 4, 123, 34]
        message = 1234
        # Possible combinations:
        # [12, 34], [123, 4], [12, 3, 4]
        self.assertEqual(count_fragment_combinations(fragments, message), 3)

    def test_no_possible_combinations(self):
        fragments = [5, 6, 7]
        message = 123
        self.assertEqual(count_fragment_combinations(fragments, message), 0)

    def test_fragments_used_once(self):
        fragments = [1, 1, 2]
        message = 112
        self.assertEqual(count_fragment_combinations(fragments, message), 2)

    def test_empty_fragments(self):
        fragments = []
        message = 1
        self.assertEqual(count_fragment_combinations(fragments, message), 0)

if __name__ == "__main__":
    unittest.main()

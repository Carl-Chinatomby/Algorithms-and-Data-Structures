import unittest

from overlap_segments import merge_and_sort


class OverlapSegementsTestCase(unittest.TestCase):
	def test_something(self):
		test_cases = (
			# testcases 1
			(	
				(
					{'start': 10, 'end': 16},
					{'start': 17, 'end': 18},
					{'start': 1, 'end': 2},
					{'start': 8, 'end': 10},
					{'start': 17, 'end': 20},
					{'start': 19, 'end': 25},
				),
				(
					{'start': 1, 'end': 2},
					{'start': 8, 'end': 16},
					{'start': 17, 'end': 25},
				),
			),
		)

		print(test_cases[0])
		for segments, expected_value in test_cases:
			actual_value = merge_and_sort(segments)
			self.assertEqual(actual_value, expected_value)

if __name__ == "__main__":
	unittest.main()
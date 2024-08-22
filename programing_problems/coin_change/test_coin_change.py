import unittest

from coin_change import number_of_ways_to_make_change


class CoinChangeTestCase(unittest.TestCase):
	def test_number_of_ways_to_make_change(self):
		test_cases = (
			# input, output
			((5, (1, 2, 3)), 5),
			((0, ()), 1),
		)

		for (amount, coins), expected_value in test_cases:
			actual_value = number_of_ways_to_make_change(amount, coins)
			self.assertEqual(actual_value, expected_value)

if __name__ == "__main__":
	unittest.main()
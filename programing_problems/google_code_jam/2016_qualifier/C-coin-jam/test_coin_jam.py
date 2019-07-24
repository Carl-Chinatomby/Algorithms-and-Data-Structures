import unittest

from coin_jam import get_jamcoins


class TestCoinJam(unittest.TestCase):
    def test_get_jamcoins(self):
        jamcoin_len = 6
        num_of_examples = 3
        jamcoins = get_jamcoins(jamcoin_len, num_of_examples)

        # Test actual_value[0]
        for jamcoin_set in jamcoins:
            jamcoin = jamcoin_set[0]

            # starts and ends with '1'
            self.assertEqual(jamcoin[0], '1')
            self.assertEqual(jamcoin[0], '1')

            # divisor of jamcoin in base
            for i in range(2, 11):
                converted_jamcoin = int(jamcoin, i)
                self.assertEqual(converted_jamcoin % int(jamcoin_set[i-1]), 0)


if __name__ == "__main__":
    unittest.main()

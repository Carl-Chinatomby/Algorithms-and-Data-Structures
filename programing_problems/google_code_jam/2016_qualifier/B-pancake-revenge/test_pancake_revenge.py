import unittest

from pancake_revenge import get_min_flips_for_pancakes, flip_pancakes


class TestPancakeRevenge(unittest.TestCase):
    def setUp(self):
        self.errors = []

    def tearDown(self):
        if self.errors:
            raise AssertionError(self.errors)

    def test_get_min_flips_for_pancakes(self):
        test_cases = (
            # input, output
            ('-', 1),
            ('-+', 1),
            ('+-', 2),
            ('+++', 0),
            ('--+-', 3),
        )

        for arrangement, expected_value in test_cases:
            actual_value = get_min_flips_for_pancakes(arrangement)
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                error_msg = "Arrangement: {arrangement} Expected: " \
                    "{expected_value} Actual: {actual_value}".format(
                        **locals())
                self.errors.append(error_msg)

    def test_flip_pancakes(self):
        test_cases = (
            # input, output
            ('-+-+-++-', '+--+-+-+'),
        )

        for arrangement, expected_value in test_cases:
            actual_value = flip_pancakes(arrangement)
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                error_msg = "Arrangement: {arrangement} Expected: " \
                    "{expected_value} Actual: {actual_value}".format(
                        **locals())
                self.errors.append(error_msg)


if __name__ == "__main__":
    unittest.main()

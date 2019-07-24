import unittest

from fractiles import (
    IMPOSSIBLE,
    get_tiles_to_reveal_gold,
)


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.errors = []

    def tearDown(self):
        if self.errors:
            raise AssertionError(self.errors)

    def run_table_test(self, test_cases, test_fct):
        for test_input, expected_value in test_cases:
            actual_value = test_fct(*test_input)
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                error_msg = "Input: {test_input} Expected: " \
                    "{expected_value} Actual: {actual_value}".format(
                        **locals()
                    )
                self.errors.append(error_msg)


class FractilesTestCase(BaseTestCase):
    def test(self):
        test_cases = (
            # input, output
            ((2, 3, 2), {2}),
            ((1, 1, 1), {1}),
            ((2, 1, 1), {IMPOSSIBLE}),
            ((2, 1, 2), {1, 2}),
            ((3, 2, 3), {2, 6}),
        )
        self.run_table_test(test_cases, get_tiles_to_reveal_gold)


if __name__ == "__main__":
    unittest.main()

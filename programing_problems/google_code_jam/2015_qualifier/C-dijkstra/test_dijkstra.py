import unittest

from dijkstra import (
    is_string_reducable,
    YES,
    NO
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


class TestDijkstra(BaseTestCase):
    def setUp(self):
        self.errors = []

    def tearDown(self):
        if self.errors:
            raise AssertionError(self.errors)

    def test_is_string_reducable(self):
        test_cases = (
            # input, output
            (('ik', 1), NO),
            (('ijk', 1), YES),
            (('kji', 1), NO),
            (('ji', 6), YES),
            (('i', 10000), NO),
        )
        self.run_table_test(test_cases, is_string_reducable)


if __name__ == "__main__":
    unittest.main()

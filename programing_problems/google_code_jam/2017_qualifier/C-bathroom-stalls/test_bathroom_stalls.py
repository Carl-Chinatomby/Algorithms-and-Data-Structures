import unittest

from bathroom_stalls import get_max_min_set


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.errors = []

    def tearDown(self):
        if self.errors:
            raise AssertionError(self.errors)

    def run_table_test(self, test_cases, test_fct):
        for test_input, expected_value in test_cases:
            actual_value = test_fct(test_input)
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                error_msg = "Input: {test_input} Expected: " \
                    "{expected_value} Actual: {actual_value}".format(
                        **locals()
                    )
                self.errors.append(error_msg)


class BathroomStallsTestCase(BaseTestCase):
    def test_get_max_min_set(self):
        test_cases = (
            # input, output
            #((10, 10), (0, 0)),
            #((11, 11), (0, 0)),
            #((4, 2), (1, 0)),
            #((5, 2), (1, 0)),
            ((6, 2), (1, 1)),
            # ((1000, 1000), (0, 0)),
            # ((1000, 1), (500, 499)),
            # ((100, 20), (0, 0)),
            # ((101, 10), (0, 0))
        )

        for input_num, expected_value in test_cases:
            actual_value = get_max_min_set(*input_num)
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                error_msg = "Input: {input_num} Expected: {expected_value} " \
                    "Actual: {actual_value}".format(**locals())
                self.errors.append(error_msg)


if __name__ == "__main__":
    unittest.main()

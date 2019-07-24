import unittest

from tidy_numbers import get_largest_tidy_number


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


class TidyNumberTestCase(BaseTestCase):
    def test_get_largest_tidy_number(self):
        test_cases = (
            # input, output
            #
            (132, 129),
            (1000, 999),
            (7, 7),
            (11111440, 11111399),
            (89999, 89999),
            (647, 599),
            (111111111111111110, 99999999999999999),
            (900, 899),
            (996, 899),
            (137549621, 136999999),
        )

        for input_num, expected_value in test_cases:
            actual_value = get_largest_tidy_number(input_num)
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                error_msg = "Input: {input_num} Expected: {expected_value} " \
                    "Actual: {actual_value}".format(**locals())
                self.errors.append(error_msg)


if __name__ == "__main__":
    unittest.main()

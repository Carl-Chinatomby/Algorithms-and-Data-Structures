import unittest
from counting_sheep import get_sleep_number, INSOMNIA


class TestCountingSheep(unittest.TestCase):
    def setUp(self):
        self.errors = []

    def tearDown(self):
        if self.errors:
            raise AssertionError(self.errors)

    def test_get_sleep_number(self):
        test_cases = (
            # input, # output
            (0, INSOMNIA),
            (1, 10),
            (2, 90),
            (11, 110),
            (1692, 5076),
        )

        for input_num, expected_value in test_cases:
            actual_value = get_sleep_number(input_num)
            error_msg = "Input: {input_num} Expected: {expected_value} " \
                "Actual: {actual_value}".format(**locals())
            try:
                self.assertEquals(expected_value, actual_value)
            except AssertionError:
                self.errors.append(error_msg)


if __name__ == "__main__":
    unittest.main()

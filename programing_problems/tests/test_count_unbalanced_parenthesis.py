#!/usr/bin/env python3

import unittest

from ..count_unbalanced_parenthesis  import get_unbalanced_count


class TestUnbalancedParentehsis(unittest.TestCase):
    def setUp(self):
        self.errors = []

    def tearDown(self):
        if self.errors:
            raise AssertionError(self.errors)

    def test_get_unbalanced_count(self):
        test_cases = (
            # test_parameter, expected_value
            (('(', ')', '(', '(', '(', '(', ')', ')', ')', '(', ')', ')'),  0),
            ((')', ')', '(', '(', ')', '(', ')', ')', '('), 3),
            (('(', ')', '(', '('), 2),
            (('(', ')', ')'), 0),
            (('(', ')', '('), 0),
        )

        for test_case, expected_value in test_cases:
            actual_value = get_unbalanced_count(test_case)
            err_msg = "Case: {test_case}, Expected: {expected_value}, " \
                " Acual: {actual_value}".format(**locals())
            try:
                self.assertEqual(expected_value, actual_value)
            except AssertionError:
                self.errors.append(err_msg)


if __name__ == "__main__":
    unittest.main()

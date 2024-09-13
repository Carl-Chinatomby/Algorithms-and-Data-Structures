"""
 Given an array

[1,2,3,4,2,0]

where each element points to the index of the next element, write a program to
determine if there is a cycle in this array.
"""
import unittest


def is_cycle(graph_lst):
    next_index = 0
    visited = [False] * len(graph_lst)
    visit_cnt = 0

    while visit_cnt < len(graph_lst) + 1 and next_index is not None:
        if visited[next_index]:
            return True
        visited[next_index] = True
        visit_cnt += 1

        # We don't want to travel ouside of bounds
        next_index = graph_lst[next_index] \
            if graph_lst[next_index] and graph_lst[next_index] < len(graph_lst) \
            else None
        if next_index is None:
            # We hit an unconnected graph, let's find the next graph
            for i in range(len(graph_lst)):
                if not visited[i]:
                    next_index = i
                    break

    return False


class TestIsCycle(unittest.TestCase):
    def test_is_cycle_table(self):
        # test_case, expected
        test_cases = (
            ([1, 2, 3, 4, 2, 0], True),
            ([1, 2, 3, 4, 5, 6], False),
            ([1, 2, 3, None, 5, 6], False),
            ([1, 2, 3, None, 4, 6], True),
            ([1, 2, 3, None, 5, 0], False),
            ([1, 2, 3, 4, 5, 4], True),
        )

        errors = []
        for test_case, expected_value in test_cases:
            try:
                self.assertEqual(is_cycle(test_case), expected_value)
            except AssertionError as e:
                errors.append({'case': test_case, 'error': e.args})

        if errors:
            print("Failed {}/{}".format(len(errors), len(test_cases)))
            raise AssertionError(errors)

        print("Passed all {} test cases".format(len(test_cases)))


if __name__ == "__main__":
    unittest.main()

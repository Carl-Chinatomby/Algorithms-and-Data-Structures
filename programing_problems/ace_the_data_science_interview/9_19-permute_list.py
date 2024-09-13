"""
Ace The Data Science Interview


Medium Problems
9.19. Citadel: Given a list of one ore more distinct integers, write a function to generate all
permutations of those integers. For example, given the input [2, 3, 4], return the following 6
permutations: [2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2].
"""
def permutate_list(lst):
    res = []
    if len(lst) <= 1:
        return [lst]
    else:
        for i in range(len(lst)): # Element E
            # recurse on previous combos
            for combo in permutate_list(lst[:i] + lst[i+1:]):
                res.append([lst[i]] + combo)
    return res


if __name__ == "__main__":
    lst = [2, 3, 4]
    expected_value = [[2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2]]

    actual_value = permutate_list(lst)
    print("Test 1: ", actual_value == expected_value,
        "actual: ", actual_value,
        "expected: ", expected_value
    )

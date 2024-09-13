"""
Ace The Data Science Interview


Medium Problems
9.15. Two Sigma: Say that there are n people. If person A is friends with person B, and person B is
friends with person C, then person A is considered an indirect friend of person  C.

Define a friend group to be any group that is either directly or indirectly friends. Given an
n-by-n adjacency matrix N, where N[i][j] is one if person i and person j are friends, and zero
otherwise, write a function to determine how many friend groups exist.
"""
def dfs(friends, i, matrix):
    friends.add(i)
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1 and j not in friends:
            dfs(friends, j, matrix)

def count_friend_groups(matrix):
    groups = 0
    friends = set()
    for i in range(len(matrix)):
        if i not in friends:
            dfs(friends, i, matrix)
            groups += 1
    return groups


if __name__ == "__main__":
    matrix = [
        [1, 1, 0],
        [1, 1, 1],
        [0, 0, 1],
    ]
    expected_value = 1

    actual_value = count_friend_groups(matrix)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )

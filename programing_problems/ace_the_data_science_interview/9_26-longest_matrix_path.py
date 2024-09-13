"""
Ace The Data Science Interview

Hard Problems
9.26. Bloomberg: Give  an m-by-n matrix with positive integers, determine the length of the longest
path of increasing integers within the matrix. For example, consider the input matrix:

[ 1 2 3
  4 5 6
  7 8 9
]

In this case, return 5, since one of the longest paths would be 1-2-5-6-9.
"""
def longest_increasing_path(matrix):
    table = {} # cache
    if len(matrix) == 0:
        return 0
    m = len(matrix)
    n = len(matrix[0])

    def dfs(i, j, prev, table):  # DFS helper
        if (i < 0 or i >= m) or j < 0 or j >= n or matrix[i][j] <= prev:
            return 0

        if (i, j) in table:
            return table[(i, j)] # get cached value

        curr_len = 1 + max(
            dfs(i-1, j, matrix[i][j], table),
            dfs(i+1, j, matrix[i][j], table),
            dfs(i, j-1, matrix[i][j], table),
            dfs(i, j+1, matrix[i][j], table),
        )
        table[(i, j)] = curr_len # save max
        return curr_len

    for i in range(m): # call DFS for each i, j
        for j  in range(n):
            dfs(i, j, -float('inf'), table) # set initial max and table

    return max(table.values())


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
    expected_value = 5

    actual_value = longest_increasing_path(matrix)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )

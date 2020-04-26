# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.


# TODO: UPDATE https://leetcode.com/articles/max-area-of-island/


def largest_island(world_map):
	seen = set()
	largest_island_cnt = 0

	def determine_current_island_size(row, column, current_size):
		print("checking", row, column)

		if (row, column) in seen:
			print("already visited", row, column)

		if world_map[row][column] == 1 and (row, column) not in seen:
			seen.add((row, column))
		else:
			seen.add((row, column))
			return 0

		l, r, b, t = 0, 0, 0, 0
		print(seen)

		try:
			if world_map[row-1][column] == 1 and 0<= row-1 < len(world_map) and 0 <=column < len(world_map[0]):# and (row-1, column) not in seen:
				l = determine_current_island_size(row-1, column, current_size)
		except:
			pass

		try:
			if world_map[row+1][column] == 1 and 0<= row+1 < len(world_map) and 0 <=column < len(world_map[0]):# and (row+1, column) not in seen:
				r = determine_current_island_size(row+1, column, current_size)
		except:
			pass

		try:
			if world_map[row][column-1] == 1 and 0<= row < len(world_map) and 0 <=column-1 < len(world_map[0]):# and (row ,column-1) not in seen:
				t = determine_current_island_size(row, column-1, current_size)
		except:
			pass

		try:
			if world_map[row][column+1] == 1 and 0<= row < len(world_map) and 0 <=column+1 < len(world_map[0]):# and (row, column+1) not in seen:
				b = determine_current_island_size(row, column+1, current_size)
		except:
			pass

		#return current_size
		return l + r + t + b + 1


	for row in range(len(world_map)):
		for column in range(len(world_map[0])):
			current_size = determine_current_island_size(row, column, 0)
			if current_size > largest_island_cnt:
				print("RESETTING", current_size)
				largest_island_cnt = current_size

	return largest_island_cnt


def maxAreaOfIsland(grid):
    seen = set()
    def area(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        return (1 + area(r+1, c) + area(r-1, c) +
                area(r, c-1) + area(r, c+1))

    return max(area(r, c)
               for r in range(len(grid))
               for c in range(len(grid[0])))


if __name__ == "__main__":
	# input, output
	test_cases = (
		(
			[[0, 0, 1, 0, 0, 0],
			 [0, 0, 1, 1, 1, 0],
			 [0, 0, 0, 0, 0, 0],
			 [0, 0, 0, 1, 0, 1],
			 [1, 0, 0, 1, 1, 1]],
			 5
		),
		(
			[[0,0,1,0,0,0,0,1,0,0,0,0,0],
			 [0,0,0,0,0,0,0,1,1,1,0,0,0],
			 [0,1,1,0,1,0,0,0,0,0,0,0,0],
			 [0,1,0,0,1,1,0,0,1,0,1,0,0],
			 [0,1,0,0,1,1,0,0,1,1,1,0,0],
			 [0,0,0,0,0,0,0,0,0,0,1,0,0],
			 [0,0,0,0,0,0,0,1,1,1,0,0,0],
			 [0,0,0,0,0,0,0,1,1,0,0,0,0]],
		 	6
		 ),
		(
			[[0,0,0,0,0,0,0,0]],
			0
		),
	)

	for world_map, expected_result in test_cases:
		actual_result = largest_island(world_map)
		assert actual_result == expected_result, "{} != {}".format(expected_result, actual_result)
from functools import lru_cache

call_counter = 0


# @lru_cache()
# def number_of_ways_to_make_change(amount, coins):
# 	"""recursive implementation"""
# 	global call_counter
# 	call_counter += 1
# 	print("call_counter: {}".format(call_counter))
# 	if not coins or amount < 0:
# 		return 0

# 	if amount == 0:
# 		return 1

# 	return number_of_ways_to_make_change(amount, coins[1:]) \
# 		+ number_of_ways_to_make_change(amount - coins[0], coins)


def number_of_ways_to_make_change(amount, coins):
	"""Iterative implementation"""
	# create matrix initialized to 0
	solutions = [ [0] * (amount+1) ] * (len(coins)+1)

	# # when amount is 0, there is 1 make to make it, which is use no coins
	for i in range(len(coins)):
		solutions[i][0] = 1


	for i in range(1, len(coins)+1):
		for j in range(1, amount+1):
			# is current coin less than what's needed?
			if coins[i - 1] <= j:
				solutions[i][j] = solutions[i-1][j] + solutions[i][j - coins[i-1]]
			else:
				solutions[i][j] = solutions[i-1][j]


	return solutions[len(coins)][amount]


if __name__ == "__main__":
	amount = 5
	coints = [1, 2, 3]
	print(number_of_ways_to_make_change(amount, coins))
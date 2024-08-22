# https://www.metacareers.com/profile/coding_practice_question/?problem_id=226517205173943&c=2162229510779671&psid=275492097255885&practice_plan=0&b=0222222


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

# O(n^2) time complexity
# O(n) space complexity
def count_subarrays(arr):
  # Write your code here

  result = [0] * len(arr)

  for idx, val in enumerate(arr):
    result[idx] += 1
    j = idx - 1
    k = idx + 1
    while j > -1 and j < len(arr):
      if arr[j] < val:
        result[idx] += 1
        j -= 1
      else:
        break


    while k > -1 and k < len(arr):
      if arr[k] < val:
        result[idx] += 1
        k += 1
      else:
        break

  return result









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)

  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

   # Add your own test cases here

  test_3 = []
  expected_3 = []
  output_3 = count_subarrays(test_3)
  check(expected_3, output_3)

  test_4 = [3, 4, 1, 2, 6]
  expected_4 = [1, 4, 1, 2, 5]
  output_4 = count_subarrays(test_4)
  check(expected_4, output_4)

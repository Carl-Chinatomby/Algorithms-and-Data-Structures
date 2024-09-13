import math
import string
# Add any extra import statements you may need here


# Add any helper functions you may need here


# Create a dictionary mapping letter to numeric
# convert input to a list
# while in place if the type(element) is a string return alpha_dict[element.lower()+rotation_value%25]  ## check this
# if type(element) is an int return element + rotation_value % 9
# else: continue

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  if not input_str:
    return input_str

  str_mapping = {v: k for k, v in enumerate(string.ascii_lowercase)}
  val_mapping = {k: v for k, v in enumerate(string.ascii_lowercase)}

  result = list(input_str)
  for idx, char in enumerate(input_str):
    if char.isalpha():
      new_val = (str_mapping[char.lower()] + rotation_factor) % 26
      result[idx] = val_mapping[new_val] if char.islower() else val_mapping[new_val].upper()
    elif char.isnumeric():
      result[idx] = str((int(char) + rotation_factor) % 10)
    else:
      continue

  return ''.join(result)











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here

  input_3 = ""
  rotation_factor_3 = 200
  expected_3 = ""
  output_3 = rotationalCipher(input_3, rotation_factor_3)
  check(expected_3, output_3)

"""
Ace The Data Science Interview


Medium Problems
9.17. Goldman Sachs: Estimate pi using a Monte Carlo method. Hint: think about throwing darts on
a square and seeing where they land within a circle.
"""
import random
import math

def get_pi():
    count = 0 # num of points inside the quarter circle
    n = 10000000 # of iterations

    for i in range(0, n):
        x_sq = random.random()**2
        y_sq = random.random()**2
        if math.sqrt(x_sq + y_sq) < 1.0: # check if inside circle:
            count += 1
    pi = (float(count) / n) * 4 # accounts for quarter circle
    return pi


if __name__ == "__main__":
    arr1 = []
    arr2 = []
    expected_value = 3.14

    actual_value = get_pi()
    print("Test 1:", round(actual_value, 2) == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )

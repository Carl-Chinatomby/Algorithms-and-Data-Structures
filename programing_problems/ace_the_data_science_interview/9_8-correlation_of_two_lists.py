"""
Ace The Data Science Interview


Medium Problems
9.8. AQR: Given two lists X and Y, return their correlation.
"""
import math

def mean(x):
    return sum(x)/len(x)

def sd(x):
    m = mean(x)
    ss = sum((i-m) ** 2 for i in x)
    return math.sqrt(ss / len(x))

def corr(x, y):
    x_m = mean(x)
    y_m = mean(y)
    xy_d = [] # product of de-meaned X and Y for covariance calc
    for i in range(len(x)):
        x_d = x[i] - x_m
        y_d = y[i] - y_m
        xy_d.append(x_d * y_d) # add product of X_i and Y_i
    return mean(xy_d) / (sd(x) * sd(y)) # from formula above


if __name__ == "__main__":
    arr1 = [3 ,5, 2, 4, 1]
    arr2 = [5 ,3, 2, 4, 1]
    expected_value = 0.5999999999999999

    actual_value = corr(arr1, arr2)
    print("Test 1: ", round(actual_value, 2) == round(expected_value, 2))

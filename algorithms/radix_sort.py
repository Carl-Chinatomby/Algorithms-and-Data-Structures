import math


def count_sort(arr, digit_num, radix=10):
    output = [0] * len(arr)
    count = [0] * radix

    for i in range(len(arr)):
        idx = (arr[i] // (radix**digit_num)) % radix
        count[idx] += 1

    for j in range(1,radix):
        # modify to have the number of elements <= i
        count[j] += count[j-1]

    for k in range(len(arr)-1, -1, -1): # go through arr backwards
        idx = (arr[k]//radix**digit_num)%radix
        count[idx] = count[idx] -1
        output[count[idx]] = arr[k]

    return output


def radix_sort(arr, radix=10):
    #radix is the base of the number system
    max_val = max(arr)
    digits = int(math.floor(math.log(max_val, radix)+1))
    for i in range(digits):
        arr = count_sort(arr, i, radix)

    return arr


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(arr)
    arr = radix_sort(arr)
    print(arr)

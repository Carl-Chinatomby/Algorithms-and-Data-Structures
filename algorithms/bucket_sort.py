import math

def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    # split elements into buckets
    for num in arr:
        buckets[int(num * 10)].append(num)

    # sort buckets
    for bucket in buckets:
        bucket.sort()

    # merge buckets
    return [elem for bucket in buckets for elem in bucket]

if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(arr)
    arr = bucket_sort(arr)
    print(arr)

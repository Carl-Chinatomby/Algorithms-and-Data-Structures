import random

def find_kth_largest(nums, k):
    return find_kth_smallest(nums, len(nums) - k)

def find_kth_smallest(nums, k):
    def partition(left, right):
        pivot = random.randint(left, right)
        nums[right], nums[pivot] = nums[pivot], nums[right]
        pivot = left
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1
        nums[right], nums[pivot] = nums[pivot], nums[right]
        return pivot

    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = partition(left, right)
        if pivot < k:
            left = pivot + 1
        elif pivot > k:
            right = pivot -1
        else:
            return nums[pivot]
    return nums[pivot]

if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    # Expected_sort = [6, 5, 4, 3, 2, 1]
    # Expected output: 5
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    # Expected sort = [6, 5, 5, 4, 3, 3, 2, 2, 1]
    # Expected output: 4


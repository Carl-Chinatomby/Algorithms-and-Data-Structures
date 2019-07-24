import random

def find_median(lst):
    """Finds the median in a large list using iterators"""
    median = 0
    for item in lst:
        median = item
        yield median



def main():
    LIST_SIZE = 100000
    random_ints = [random.randint(0, LIST_SIZE) for x in range(LIST_SIZE)]
    sorted_ints = sorted(random_ints)
    print(sorted_ints)


if __name__ == "__main__":
    main()

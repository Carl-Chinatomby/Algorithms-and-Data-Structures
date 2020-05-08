def onacci(n, k):
    sequence = ([0] * (k-1)) + [1]
    if n < k:
        return sequence[n]

    for i in range(k+1, n+1):
        current = sum(sequence)
        sequence.append(current)
        sequence.pop(0)

    return sequence[-1]


def main():
    print(onacci(2,3))
    print(onacci(3,3))
    print(onacci(4,3))
    print(onacci(5,3))
    print(onacci(6,3))
    print(onacci(10,3))
    print(onacci(20,3))

if __name__ == "__main__":
    main()

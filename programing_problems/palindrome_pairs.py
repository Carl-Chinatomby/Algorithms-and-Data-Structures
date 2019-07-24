"""Find pairs of palindromes in a list"""


def get_palindrome(word):
    return word[::-1]


def get_palindrone_pairs_equal_length(words):
    """only works if the words are equal length"""
    palindrome_lookup = {}
    results = []

    for word in words:
        palindrome = get_palindrome(word)
        if word not in palindrome_lookup:
            palindrome_lookup[palindrome] = ('{}{}'.format(word, palindrome), '{}{}'.format(palindrome, word))
        else:
            results.append(palindrome_lookup[word])

    return results

def is_palindrome(word):
    return word[::-1] == word


def get_palindrome_pairs(words):
    """Brute face that covers all possibilities"""
    return ['{}{}'.format(word1, word2) for word1 in words for word2 in words \
        if word1 != word2 and is_palindrome('{}{}'.format(word1, word2))]


def get_palindrome_pairs_w_indices(words):
    return [('{}{}'.format(word1, word2), (index1, index2))
        for index1, word1 in enumerate(words)
            for index2, word2 in enumerate(words)
                if word1 != word2 and is_palindrome('{}{}'.format(word1, word2))]

def main():
    words = ["bat", "tab", "cat"]
    #words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(get_palindrome_pairs_w_indices(words))


if __name__ == "__main__":
    main()

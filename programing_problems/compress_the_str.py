def get_char_count(string):
    current_char = None
    current_count = 0
    counts = []
    for c in string:
        if current_char and c != current_char:
            counts.append((current_count, int(current_char)))
            current_char = c
            current_count = 0

        current_char = c
        current_count += 1

    counts.append((current_count, int(current_char)))
    
    return counts
    


if __name__ == "__main__":
    #string = input()
    string = '1222311'
    for val in get_char_count(string):
        print(val, end=' ')

    # expected output: (1, 1) (3, 2) (1, 3) (2, 1)

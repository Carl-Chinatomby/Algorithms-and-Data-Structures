import os


def print_dir_tree(path, level=0, indent=4):
    for file in sorted(os.scandir(path), key=lambda f: (not f.is_dir(), f.name)):
        if file.name.startswith('.'):
            continue
        elif file.is_dir():
            print('{}-{}'.format(' '*level*indent, file.name))
            print_dir_tree(file, level+1, indent)
        else:
            print('{}{}'.format(' '*level*indent, file.name))


def main():
    #path = '/Users/carlchinatomby'
    path = '/Users/carlchinatomby/Desktop/development/projects/git/Algorithms-and-Data-Structures/programing_problems'
    print_dir_tree(path)


if __name__ == "__main__":
    main()

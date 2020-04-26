#!/usr/bin/env python3
"""
Problem

Long ago, the Fractal civilization created artwork consisting of linear rows of tiles. They had two types of tile that they could use: gold (G) and lead (L).

Each piece of Fractal artwork is based on two parameters: an original sequence of K tiles, and a complexity C. For a given original sequence, the artwork with complexity 1 is just that original sequence, and the artwork with complexity X+1 consists of the artwork with complexity X, transformed as follows:

replace each L tile in the complexity X artwork with another copy of the original sequence
replace each G tile in the complexity X artwork with K G tiles
For example, for an original sequence of LGL, the pieces of artwork with complexity 1 through 3 are:

C = 1: LGL (which is just the original sequence)
C = 2: LGLGGGLGL
C = 3: LGLGGGLGLGGGGGGGGGLGLGGGLGL
Here's an illustration of how the artwork with complexity 2 is generated from the artwork with complexity 1:



You have just discovered a piece of Fractal artwork, but the tiles are too dirty for you to tell what they are made of. Because you are an expert archaeologist familiar with the local Fractal culture, you know the values of K and C for the artwork, but you do not know the original sequence. Since gold is exciting, you would like to know whether there is at least one G tile in the artwork. Your budget allows you to hire S graduate students, each of whom can clean one tile of your choice (out of the KC tiles in the artwork) to see whether the tile is G or L.

Is it possible for you to choose a set of no more than S specific tiles to clean, such that no matter what the original pattern was, you will be able to know for sure whether at least one G tile is present in the artwork? If so, which tiles should you clean?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with three integers: K, C, and S.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if no set of tiles will answer your question, or a list of between 1 and S positive integers, which are the positions of the tiles that will answer your question. The tile positions are numbered from 1 for the leftmost tile to KC for the rightmost tile. Your chosen positions may be in any order, but they must all be different.

If there are multiple valid sets of tiles, you may output any of them. Remember that once you submit a Small and it is accepted, you will not be able to download and submit another Small input. See the FAQ for a more thorough explanation. This reminder won't appear in problems in later rounds.

Limits

1 ≤ T ≤ 100.
1 ≤ K ≤ 100.
1 ≤ C ≤ 100.
KC ≤ 1018.

Small dataset

S = K.
Large dataset

1 ≤ S ≤ K.
Sample


Input

Output

5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3

Case #1: 2
Case #2: 1
Case #3: IMPOSSIBLE
Case #4: 1 2
Case #5: 2 6

Note: for some of these sample cases, other valid solutions exist.

In sample case #1, there are four possible original sequences: GG, GL, LG, and LL. They would produce the following artwork, respectively:

Original sequence GG: GGGGGGGG
Original sequence GL: GGGGGGGL
Original sequence LG: LGGGGGGG
Original sequence LL: LLLLLLLL
One valid solution is to just look at tile #2. If tile #2 turns out to be G, then you will know for sure the artwork contains at least one G. (You will not know whether the original sequence is GG, GL, or LG, but that doesn't matter.) If tile #2 turns out to be L, then you will know that the original sequence must be LL, so there are no Gs in the artwork. So 2 is a valid solution.

On the other hand, it would not be valid to just look at tile #1. If it turns out to be L, you will only know that the original sequence could have been either LG or LL. If the original sequence is LG, there is at least one G in the artwork, but if the original sequence is LL, there are no Gs. So 1 would not be a valid solution.

Note that 1 2 is also a valid solution, because tile #2 already provides all the information you need. 1 2 3 is not a valid solution, because it uses too many tiles.

In sample case #2, the artwork must consist of only one tile: either G or L. Looking at that tile will trivially tell you whether or not the artwork has a G in it.

In sample case #3, which would not appear in the Small dataset, the artwork must be either GG, GL, LG, or LL. You can only look at one tile, and neither of them on its own is enough to answer the question. If you see L for tile #1, you will not know whether the artwork is LG or LL, so you will not know whether any Gs are present. If you see L for tile #2, you will not know whether the artwork is GL or LL, so you will not know whether any Gs are present.

Sample case #4 is like sample case #3, but with access to one more tile. Now you can just look at the entire artwork.

In sample case #5, there are eight possible original sequences, and they would produce the following artwork:

Original sequence GGG: GGGGGGGGG
Original sequence GGL: GGGGGGGGL
Original sequence GLG: GGGGLGGGG
Original sequence GLL: GGGGLLGLL
Original sequence LGG: LGGGGGGGG
Original sequence LGL: LGLGGGLGL
Original sequence LLG: LLGLLGGGG
Original sequence LLL: LLLLLLLLL
One valid solution is to look at tiles #2 and #6. If they both turn out to be Ls, the artwork must be all Ls. Otherwise, there must at least one G. Note that 1 2 would not be a valid solution, because even if those tiles both turn out to be Ls, that does not rule out an original sequence of LLG. 6 2 would be a valid solution, since the order of the positions in your solution does not matter.
"""
import argparse
from itertools import product


IMPOSSIBLE = 'IMPOSSIBLE'


# def get_tiles_to_reveal_gold(original_length, complexity, num_of_tiles):
#     """
#         :returns :set
#             A set of the either 1 to 5 integers revealing which tiles will be
#             needed to answer if there's a gold tile. If no such sequence exists
#             returns a (IMPOSSIBLE,)

#         :param :int original_length: The length of the original sequence
#         :param :int complexity: The complexity of the current sequence
#         :param :int num_of_tiles: The number of tiles that cna be revealed
#     """
#     # Create array of possilities
#     # create position -> count for those L's
#     # sort by #'s of L's, peak and remove possibilies
#     # if possibilies == 0 return sequence
#     # elif out of num_of tiles return impossible
#     # else repeat

#     # if original_length == 1:
#     #     return [1]
#     # originals = [x for x in product('GL', repeat=original_length)]
#     # artworks = []
#     # for original in originals:
#     #     artwork = []
#     #     for tile in original:
#     #         if tile == 'G':
#     #             artwork.extend(['G'] * original_length)
#     #         else:
#     #             artwork.extend(original)
#     #     artworks.append(tuple(artwork))

#     # removed = 0

#     # tile_order = []
#     # while num_of_tiles:
#     #     l_count = [[0, -1, []] for x in range(len(artworks[0]))]
#     #     for x in range(len(artworks[0])):
#     #         for y in range((2 ** original_length) - removed):
#     #             if artworks[y][x] == 'L':
#     #                 l_count[x][0] += 1
#     #                 l_count[x][1] = x
#     #             else:
#     #                 l_count[x][2].append(artworks[y])

#     #     ordered_artwork = sorted(l_count, key=lambda k: k[0])
#     #     if l_count[0][0] > 1:
#     #         num_of_tiles -= 1
#     #         tile_order.append(ordered_artwork[0][1] + 1)
#     #         for artwork in ordered_artwork[0][2]:
#     #             artworks.remove(artwork)
#     #             removed += 1
#     #     else:
#     #         return tile_order

#     total_len = original_length ** complexity
#     if num_of_tiles == original_length:
#         return [i + 1 for i in range(0, original_length)]

#     return IMPOSSIBLE


def get_tiles_to_reveal_gold(original_length, complexity, num_of_tiles):
    sequence = []
    if original_length == num_of_tiles:
        x = 1
        sequence.append(1)
        for i in (1, original_length**complexity, original_length):
            sequence.append(i + x + original_length)
            x += 1
        print(sequence)
        return sequence

    return IMPOSSIBLE

def main(filepath):
    outfile_name = filepath.replace('.in', '.out') if '.in' in filepath \
        else filepath + '.out'
    with open(filepath) as infile, open(outfile_name, 'w') as outfile:
        num_of_test_cases = int(infile.readline().strip())
        for i in range(1, num_of_test_cases+1):
            row = infile.readline().strip().split()
            original_length = int(row[0])
            complexity = int(row[1])
            num_of_tiles = int(row[2])
            tile_seq = get_tiles_to_reveal_gold(
                original_length,
                complexity,
                num_of_tiles
            )
            print("FINAL ANSWER {}".format(tile_seq))
            outfile.write('Case #{}: {}\n'.format(i, " ".join(
                str(tile) for tile in tile_seq
            )))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="Filepath to the input filename")
    args = parser.parse_args()

    main(filepath=args.infile)

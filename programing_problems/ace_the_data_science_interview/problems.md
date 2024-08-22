"""
Ace The Data Science Interview


Easy Problems
9.1. Amazon: Given two arrays, write a function to get the intersection of the two. For example,
if A = [1, 2, 3, 4, 5], and B = [0, 1, 3, 7] then you should return [1, 3]

9.2. D.E. Shaw: Given an integer array, return the maximum product of any three numbers in
the array. For example, for A = [1, 3,4, 5], you should return 60, while B = [-2, -4, 5, 3] you
should return 40.

9.3. Facebook: Given a list of coordinates, write a function to find the k closest points (measured by
Euclidean distance) to the origin. For example if k = 3, and the points are [[2, -1], [3, 2],
[4m 1], [-1, -1], [-2, 2]], then return [[-1, -1], [2, -1], [-2, 2]].

9.4. Google: Say you have an n-by-n matrix of elements that are sorted in ascending order both
in the columns and rows of the matrix. Return the k-th smallest elemnt of the matrix for
example, consider the matrix below:

[1 4 2
 2 5 9
 6 8 11
]

If k = 4, then return 5.

9.5. Akuna Capital: Given an integer array, find the sum of the largest contiguous subarray within
the array. For example, if the input is [-1, -3, 5, -4, 3 -6, 9, 2], then return 11 (because of
[9, 2]). Not that if all the elements are negative you should return 0.

9.6. Facebook: Given a binary tree, write a function to determine whether the tree is a mirror image
of itself. Two trees are mirror image of each other if their root values are the same and left
subtree is a mirror image of the right subtree.

Medium Problems
9.7. Google: Given an array of positive integers, a peak element is greater than it's neighbors. Write
a function to find the index of any peak elements. For example, for [3 ,5, 2, 4, 1], you should
return either 1 or 3 because the values at those indexes, 5 and 4,  are both peak elements.

9.8. AQR: Given two lists X and Y, return their correlation.

9.9. Amazon: Given a binary tree, write a function to determine the diameter of the tree, which is
the longest paths between any two nodes.

9.10. D.E. Shaw: Given a target number, generate a random sample of n integers that sum in that
target that also are within sigma standard deviations of the mean.

9.11. Facebook: You have the entire social graph of Facebook users, with nodes representing users
and edges representing friendships between users. Given a social graph and two users as
input, write a function to return the smallest number of friendships, between two users. For
example, take the graph that consists of 5 users A, B, C, D, E and the friendship edges are:
(A, B), (A, C), (B, D), (D, E). If the two input users are A and E, then the function should return 3
since A is friends with B, B is friends with D, and D is friends with E.

9.12. LinkedIn: Given two strings A and B, write a function to return a list of all the start indices
within A where the substring of A is an anagram of B. For example, if A = "abcdebac" and
B = "abc", then you want to return [0, 4, 5] since those are the starting indices of substrings of
A that are anagrams of B.

9.13. Yelp: You are given an array of intevals, where each interval is represented by a start time
and an end time, such as [1, 3]. Determine the smallest number of intervals to remove from
the list, such that the rest of the intervals do not overlap. Intervals can "touch," such as [1, 3]
and [3, 5], but are not allowed to overlap, such as [1, 3] and  [2, 5]). FOr example, if the input
interval  list given is: [[1, 3], [3, 5], [2, 4], [6, 8]], then return 1, since the interval [2, 4]
should be removed.

9.14. Goldman Sachs: Given an array of strings, return a list of lists where each list contains the
strings that are anagrams of one another. For example, if the input is ["abc", "abd", "cab",
"bad", "bca", "acd"] then return: [["abc", "cab", "bca"], ["abd", "bad", "acd"]].

9.15. Two Sigma: Say that there are n people. If person A is friends with person B, and person B is
friends with person C, then person A is considered an indirect friend of person  C.

Define a friend group to be any group that is either directly or indirectly friends. Given an
n-by-n adjacency matrix N, where N[i][j] is one if person i and person j are friends, and zero
otherwise, write a function to determine how many friend groups exist.

9.16. Workday: Given a linked list, return the head of the same linked list but with k-th node from
the end of a linked list removed. For example, given the linked list 3 -> 2 -> 5 -> 1 -> 4 and k = 3,
remove the 5 node and thus, return the linked list 3 -> 2-> 1 -> 4.

9.17. Goldman Sachs: Estimate pi using a Monte Carlo method. Hint: think about throwing darts on
a square and seeing where they land within a circle.

9.18. Palantir: Given a string with lowercase letters and left and right parenthesis, remove the
minimum number of parenthesis so that the string is valid (every left parenthesis is correctly
matched by a corresponding right parenthesis). For example, if the  string is ")a(b((cd)e(f)g"
then return is "ab((cd)e(f)g)"

9.19. Citadel: Given a list of one ore more distinct integers, write a function to generate all
permutations of those integers. For example, given the input [2, 3, 4], return the following 6
permutations: [2, 3, 4], [2, 4, 3], [3, 2, 4], [3, 4, 2], [4, 2, 3], [4, 3, 2].

9.20. Two Sigma: Given a list of several categories (for example, the strings A, B, C, and D), sample
from the list of categories according to a particular relative weighting scheme. For example,
say we give A a relative weight of 5, B a weight of 10, C a weight of 15, and D a weight of 20,
How do we construct this sampling? How do you extend the solution to an arbitrary large number of
k categories?

9.21. Amazon: Given two arrays with integers, return the maximum length of a common subarray
within both arrays. For example, if the two arrays are [1, 3, 5, 6, 7] and [2, 4, 3, 5, 6] then
return 3, since the length of the maximum common subarray, [3, 5, 6] is 3.

9.22. Uber: Given a list of positive integers, return the maximum increasing subsequence sum. In
other words, return the sum of the largest increasing subsequence with the input array. For
example, if the input is [3, 2, 5, 7, 6], return 15 because it's the sum of 3, 5, 7. If the input is
[5, 4, 3, 2, 1], return 5 (since no subsequence is increasing).

9.23. Palantir: Given a positive integer n, find the smallest number of perfect squares that sum up to
n. For example, for n = 7, you should return 4, since 7 = 4 + 1 + 1 + 1.  For n = 13, you should
return 2, since 13 = 9 + 4.

9.24. Faebook: Given an integer n and an integer k, output a list of all the combinations of k
numbers chosen from 1 to n. For example, if n = 3 and k = 2, return [1, 2], [1, 3], [2, 3].

Hard Problems
9.25. Citadel: Given a string with left and right parenthesis, write a function to determine the length
of the longest well-formed substring. For example, if the input string is ")(()(", then return 4,
since the longest well-formed string is "(())".

9.26. Bloomberg: Given  an m-by-n matrix with positive integers, determine the length of the longest
path of increasing integers within the matrix. For example, consider the input matrix:

[ 1 2 3
  4 5 6
  7 8 9
]

In this case, return 5, since one of the longest paths would be 1-2-5-6-9.

9.27. Google: Given a number n, return the number of lists  of consecutive positive integers that sum
up to n. For example, for n = 9, return 3, since the consecutive positive integer lists are
[2, 3, 4], [4, 5], and [9]. Can you solve this in linear time?

9.28. Citadel: Given an continuous stream of integers, write a class with functions to add new integers
to the stream, and a function to calculate the median at any time.

9.29. Two Sigma: Given an input string and a regex, write a function that checks whether  the regex
matches the input string.  The input string is composed of the lowercase letters a-z. The regular
expression contains lowercase a-z, '?' or '*', where the '?' matches any one character, and the '*'
maatches any arbitrary number of characters (empty as well). For example, if the input string
is "abcdba" and the regex is "a*c?*", return true. However, if the regex was instead "b*c?*"
return false.

9.30. Citadel: A fire department wants to build a new fire station in a location where the total
distance from the station to all houses in the town (in Euclidean terms) is minimized. Given a list of
coordinates for the n houses, return the coordinates of the optimal location for the new fire station.
"""

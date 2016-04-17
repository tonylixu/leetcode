Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.

This is really an easy problem to solve. The simplest solution I can think of
is keep dividing and mod number by 10. Dividing will give your the first digit,
for example:
38 = 3(38/10) + 8(38%10) = 11
381 = 38(381/10) + 1(381%10) = 39 = 3(39/10) + 9(39%10) = 12
as you can see, it can be boiled down to 3(39/10) + 9, wich is 8 + 1.

Challenge (solution-final.py) :
Could you do it without any loop/recursion in O(1) runtime?

If you look at the following examples:
in  out  in  out
0   0    10  1
1   1    11  2
2   2    12  3
3   3    13  4
4   4    14  5
5   5    15  6
6   6    16  7
7   7    17  8
8   8    18  9
9   9    19  1

You can find a pattern here, except "0", any other numbers can be written as:
10 = 1 + 1 x 9
12 = 2 + 1 x 9
13 = 4 + 1 x 9
..
38 = 2 + 4 x 9

So if a number can be mod by 9, the output is 9, otherwise it will be the
reminder

You can can ust return num % 9 if the number is not 0 or multiple of 9.

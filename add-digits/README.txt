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

Challenge (Still thinking about it):
Could you do it without any loop/recursion in O(1) runtime?

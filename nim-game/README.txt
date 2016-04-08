You are playing the following Nim Game with your friend: There is a heap of
stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first
turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a
function to determine whether you can win the game given the number of stones
in the heap.

For example, if there are 4 stones in the heap, then you will never win the
game: no matter 1, 2, or 3 stones you remove, the last stone will always be
removed by your friend.

Hint:

If there are 5 stones in the heap, could you figure out a way to remove the
stones such that you will always be the winner?

As you can see, as long as you can leave 4 stones in the heap, you can almost
gurantee you can win. For example, let say there are 5 stones in the heap, in
your first move, you can remove 1 stone, then player2 will have 4 stones in the
heap. No matter what the number of stones player2 removes, the last stone will
always be removed by you.

It all comes to the point that if the number of stones in the heap is a
multiplier of 4 (4, 8, 12, 16 ..etc), you will lose no matter what (player2 is
clever enough to always leave 4xn stones in the heap for you).

So if the number of stones % 4 is 0, you can not win.

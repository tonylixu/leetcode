stones = int(13)
player_number = int(0)

while (stones > 0 ):
    if (player_number %2 != 1) :
        player_move = int(raw_input("Player one, please enter your move:"))
        if (player_move > 0 ) and (player_move < 3) and (player_move <= stones):
            stones = stones - player_move
            player_number += 1
            print("Stones in the heap is {}".format(stones))
        else:
            print("Illegal move. Try again.")
    else:
        player_move = int(raw_input("Player two, please enter your move:"))
        if (player_move > 0 ) and (player_move < 3) and (player_move <= stones):
            stones = stones - player_move
            player_number += 1
            print("Stones in the heap is {}".format(stones))

winner = int(player_number % 2)

if (winner != 1):
    print "Congratulations player 1"
else:
    print "Congratulations player 2"

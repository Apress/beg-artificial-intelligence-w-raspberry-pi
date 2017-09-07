sticks = 21
max_picks = 3



while (sticks != 0):
    pick1 = 0
    pick2 = 0
   
    pick1 = int(raw_input("Player 1 pick: "))
    while pick1 > max_picks or (sticks - pick1) <= 0:
        print "You cannot pick more then 3 or reduce sticks to zero or less"
        pick1 = int(raw_input("Player 1 pick: "))
    sticks =  sticks - pick1
    print "remaining sticks = ", sticks
    if sticks == 1:
        print 'Player 1 Wins!'
        exit()
    
    pick2 = int(raw_input("Player 2 pick: "))
    while pick2 > max_picks or (sticks - pick2) <= 0:
        print "You cannot pick more than 3 or reduce sticks to zero or less"
        pick2 = int(raw_input("Player2 pick: "))
    sticks = sticks - pick2
    print "remaining sticks = ", sticks
    if sticks == 1:
        print 'Player 2 Wins!'
        exit()

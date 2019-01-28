from Board import Board

if __name__ == "__main__":
    print('# Select Board Size')
    board_size = input("board size: ")
    print('# Select Number of Mines')
    mines_size = input("mines: ")
    #board size = 5
    #mines size = 2
    b = Board(int(board_size), int(mines_size))
    #print(b)
    while b.status == "running":
        m = input("move: ")
        pair = m.split(',')
        print(b.move(int(pair[0]),int(pair[1])))
    print('game close')

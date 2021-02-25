#----------tic tac toe-------------
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
number_list = []
def game_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8]+"\n")

def add_x(pos):
    board[pos-1]= "X"
    game_board()

def add_0(pos):
    board[pos-1] = "0"
    game_board()

def winner():
    won = row() or col() or diagonal()
    try:
        if won[0]:
            print(f"The winner is {won[1]}")
        return won[0]
    except:
        pass

def row():
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1:
        return True, board[0]
    elif row2:
        return True, board[3]
    elif row3:
        return True, board[6]

def col():
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1:
        return True, board[0]
    elif col2:
        return True, board[1]
    elif col3:
        return True, board[2]

def diagonal():
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 :
        return True, board[0]
    elif diagonal2:
        return True, board[2]

print(board)
game_board()
for i in range(1,10):
    if i%2 == 1:
        num = int(input("Position to add X - "))
        if (num not in number_list) and num<10:
            add_x(num)
            number_list.append(num)
        else:
            print("Restart")
            break
    else :
        num = int(input("Position to add Y - "))
        if (num not in number_list) and num <10:
            add_0(num)
            number_list.append(num)
        else:
            print("Restart")
            break

    if winner():
        break

print("Draw")
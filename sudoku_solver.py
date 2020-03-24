def solve_board(board):
    if(solve_board_helper(board)==True):
        return True

def solve_board_helper(board):
    result=find_empty(board)
    if not result:
        print_board(board)
        return True
    else:
        row,col=result

        for num in range(1,10):
            if(check_valid(board,row,col,num)==True):
                #print(row,col)
                board[row][col]=num


                if(solve_board(board)==True):
                    return True
                else:
                    board[row][col]=0
        return False



def find_empty(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                return i,j
    return None


def check_valid(board,curr_row,curr_col,val):
    for col in range(9):
        if(board[curr_row][col]==val and col!=curr_col):
            return False

    for row in range(9):
        if(board[row][curr_col]==val and row!=curr_row):
            return False

    box_start_row = (curr_row // 3) * 3
    box_start_col = (curr_col // 3) * 3
    #print(curr_row,curr_col,box_start_row,box_start_col )
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if (i != curr_row and j != curr_col):
                if (board[i][j] == val):
                    return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")



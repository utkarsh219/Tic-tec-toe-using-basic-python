board=[' ' for _ in range(10)]
def insert(element,position):
    board[position]=element
def printBoard(board):
    print('   |  |  ')
    print(' '+ board[1] + ' | ' + board[2] + '| '+ board[3] +' ')
    print('   |  |  ')
    print('------------')
    print('   |  |  ')
    print(' '+ board[4] + ' | ' + board[5] + '| '+ board[6] +' ')
    print('   |  |  ')
    print('------------')
    print('   |  |  ')
    print(' '+ board[7] + ' | ' + board[8] + '| '+ board[9] +' ')
    print('   |  |  ')
def isboardfull(board):
    if(board.count(' ')>1):
        return False
    else:
        return True
def freespace(position):
    return board[position]==' '
def Winner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def player():
    t=True
    while t:
        move=int(input("Enter the position between(1-9) "))
        try:
            if(move>0 and move<10):
                if(freespace(move)):
                    t=False
                    insert('X',move)
                else:
                    print("This position is occupied,Try another")
            else:
                print("Enter valid number")
        except:
            print("Enter Only numbers")
def computer():
    valid_position=[x for x,letter in enumerate(board) if letter==' ']
    move=0
    for let in ['O','X']:
        for i in valid_position:
             board1=board[:]
             board1[i]=let
             if(Winner(board1,let)):
                 move=i
                 return move
    cornor=[]
    for i in valid_position:
        if i in [1,3,7,9]:
            cornor.append(i)
    if(len(cornor)>0):
        move=Select_Random(cornor)
        return move
    if 5 in valid_position:
        move=5
        return move
    edges=[]
    for i in valid_position:
        if i in [2,4,6,8]:
            edges.append(i)
    if(len(edges)>0):
        move=Select_Random(edges)
        return move
    else:
        return move
def Select_Random(list1):
    import random
    r=random.randrange(0,len(list1))
    return list1[r]
def main():
    print("Welcome to the Tic Toc Toe Game")
    printBoard(board)

    while not(isboardfull(board)):
        if not(Winner(board,'O')):
            player()
            printBoard(board)
        else:
            print("Sorry you Loss")
            break
        if not(Winner(board,'X')):
            move=computer()
            if(move==0):
                print(" ")
                break
            else:
                insert('O',move)
                print("Computer is placed on the position",move,':')
                printBoard(board)
        else:
            print("You Win")
            break
    if(isboardfull(board)):
        print("Match Tie")
while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break

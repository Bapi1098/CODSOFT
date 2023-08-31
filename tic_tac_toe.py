Board={
    1:'',2:'', 3:'',
    4:'', 5:'', 6:'',
    7:'', 8:'', 9:'',
}
you= 'X'
bot='O'
def printBoard(Board) :
    print(Board[1]+'  |  '+ Board[2]+'  |  '+Board[3])
    print("_______________")
    print(Board[4]+'  |  '+ Board[5]+'  |  '+Board[6])
    print("_______________")
    print(Board[7]+'  |  '+ Board[8]+'  |  '+Board[9])

printBoard(Board)

def spaceIsFree(position):
    if (Board[position] == ''):
        return True
    else:
        return False

def checkforDraw():
    for key in Board.keys():
        if Board[key] =='':
            return False
    return True

def checkforWin():
    if (Board[1]==Board[2] and Board[1]==Board[3]and Board[1]!=''):
        return True
    elif (Board[4]==Board[5] and Board[4]==Board[6]and Board[4]!=''):
        return True
    elif (Board[7]==Board[8] and Board[7]==Board[9]and Board[7]!=''):
        return True
    elif (Board[1]==Board[4] and Board[1]==Board[7]and Board[1]!=''):
        return True
    elif (Board[2]==Board[5] and Board[2]==Board[8]and Board[2]!=''):
        return True
    elif (Board[3]==Board[6] and Board[3]==Board[9]and Board[3]!=''):
        return True
    elif (Board[1]==Board[5] and Board[1]==Board[9]and Board[1]!=''):
        return True
    elif (Board[3]==Board[5] and Board[3]==Board[7]and Board[3]!=''):
        return True
    elif (Board[7]==Board[5] and Board[7]==Board[3]and Board[7]!=''):
        return True
def checkWin(Bapi):
    if (Board[1]==Board[2] and Board[1]==Board[3]and Board[1]!=Bapi):
        return True
    elif (Board[4]==Board[5] and Board[4]==Board[6]and Board[4]!=Bapi):
        return True
    elif (Board[7]==Board[8] and Board[7]==Board[9]and Board[7]!=Bapi):
        return True
    elif (Board[1]==Board[4] and Board[1]==Board[7]and Board[1]!=Bapi):
        return True
    elif (Board[2]==Board[5] and Board[2]==Board[8]and Board[2]!=Bapi):
        return True
    elif (Board[3]==Board[6] and Board[3]==Board[9]and Board[3]!=Bapi):
        return True
    elif (Board[1]==Board[5] and Board[1]==Board[9]and Board[1]!=Bapi):
        return True
    elif (Board[3]==Board[5] and Board[3]==Board[7]and Board[3]!=Bapi):
        return True
    elif (Board[7]==Board[5] and Board[7]==Board[3]and Board[7]!=Bapi):
        return True
    
def insertLetters(letter, position):
    if spaceIsFree(position):
        Board[position] = letter
        printBoard(Board)
        if (checkforDraw()):
            print("Draw!")
            exit()

        if checkforWin():
            if letter=='X':
                print("You Won!")
                exit()
            else:
                print("Bot's Victory!")
                exit()

    else:
        print("can't insert there")
        position=int(input("Have a new chance: "))
        insertLetters(letter,position)
        return

def yourMove():
    position = int(input("Enter Your Move: "))
    insertLetters(you,position)
    return

def botMove():
    value = -10000
    bestMove=0
    print("bot's move: ")

    for key in Board.keys():
        if(Board[key]==''):
            Board[key]=bot
            score = miniMax(Board,False)
            Board[key] =''
            if(score > value):
                value=score
                bestMove = key
    insertLetters(bot,bestMove)
    return

def miniMax(Board, isMaximising):
    if checkWin(bot):
        return 1
    elif checkWin(you):
        return -1
    elif checkforDraw():
        return 0 
    if isMaximising:
        value = -10000
        
        for key in Board.keys():
            if(Board[key]==''):
                Board[key]=bot
                score = miniMax(Board,False)
                Board[key] =''
                if(score > value):
                    value=score
        return value
    else:
        value = 100
        
        for key in Board.keys():
            if(Board[key]==''):
                Board[key]=you
                score = miniMax(Board,True)
                Board[key] =''
                if(score < value):
                    value=score
        return value

while not checkforWin():
    yourMove()
    botMove()
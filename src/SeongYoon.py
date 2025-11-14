graphBoard = [['□' for x in range(15)] for j in range(15)]
Y_ORIGIN = 14

def drawGraphBoard():
    for row in graphBoard:
        print("  ".join(row))

def showLinearGraph(*args):
    
    def setPoint(y,x):
        if 0<=x<15 and 0<= y < 15:
             graphBoard[y][x] = "■"

    if len(args) == 1:
        constants = args[0]
        for col in range(len(graphBoard[0])):
            setPoint(Y_ORIGIN-constants,col)

    elif len(args) == 2:
        constants = args[0]
        first_arg = args[1]
        for i in range(len(graphBoard[0])):
            setPoint(Y_ORIGIN-(i*first_arg+constants),i)

    elif len(args) == 3:
        constants = args[0]
        first_arg = args[1]
        second_arg = args[2]
        for i in range(len(graphBoard[0])):
            setPoint(Y_ORIGIN-(second_arg*(i**2)+i*first_arg+constants),i)
    drawGraphBoard()


showLinearGraph(5)
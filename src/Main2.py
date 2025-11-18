def leftclick():
    if(board_open[x][y] == True):
        #낫띵
        return
    if(board_close[x][y] == True):
        #재귀저기연산 시작
        return
    if(board[x][y]==mine):
        #calling gameover 
        return
    
def rightclick():
    if(board[x][y]==nonclick):
        #깃발 생성
        return
    if(board[x][y]==flag):
        #깃발 제거
        return
    if(board[x][y]==mine):
        #깃발과 지뢰의 수가 동일한지? 동일하면 승리
        return
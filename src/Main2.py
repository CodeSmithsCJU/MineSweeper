#mine = -1
#flag = -2
#b1 = 답지
#b2 = 문제지
# col = j row = i
#답지는 폭탄 -1과 숫자로 써져있는 완성된 배열
#풀이는 연산 시행 부분 대조한 뒤 가져오기
def leftclick():
    if(b_open[j][i] == True):
        #낫띵해쁜드
        return
    if(b_close[j][i] == True):
        if(1 <= b1[j][i] <= 8):
            #답지 칸 번호 불러오기
            return
        if(b1[j][i] == -2):
            # 깃발 없애고 판단 시작?
            return
        if(b1[j][i] == 0):
            #재귀적연산 시작
            return
        if(b1[j][i] == -1):
            #calling gameover 
            return
        return
    
def rightclick():
    if(b[j][i]==b_close):
        #깃발 이미지로 변경
        return
    if(b[j][i] == -2):
        #칸 기본 이미지로 변경
        return
    if(b[j][i] == -1):
        if(-1 == -2):
            #게임 승리 불러오기
            return
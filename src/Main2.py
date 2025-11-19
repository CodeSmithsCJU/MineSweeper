#mine = -1
#flag = -2
#b1 = 답지
#b2 = 문제지
# col = j row = i
clear = 0
#답지는 폭탄 -1과 숫자로 써져있는 완성된 배열
#풀이는 연산 시행 부분 대조한 뒤 가져오기
def leftclick():
    if(b_open[j][i] == True):  #낫띵해쁜드
        return
    
    if(b_2[j][i] == NaN):
        if(b2[j][i] == -2):
            # 깃발 
            return
        if(1 <= b1[j][i] <= 8):#답지 칸 번호 배열 불러오기
            b2[j][i] = b1[j][i]
            return
        if(b1[j][i] == -1):
            clear = 2 
            return
        if(b1[j][i] == 0):
            repeat()
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
            clear = 1
            return
        
arr = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1), ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)]

def repeat():
    try:
        for i in range(8):
    except:
        a #테두리 칸 그거 어쩌구
    return
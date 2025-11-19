#mine = -1
#flag = -2
#b1 = 답지
#b2 = 문제지
# col = j row = i

arr = [(-1, -1), (-1, 0), (-1, 1),( 0, -1), ( 0, 1),( 1, -1), ( 1, 0), ( 1, 1)]
#답지는 폭탄 -1과 숫자로 써져있는 완성된 배열
#풀이는 연산 시행 부분 대조한 뒤 가져오기
def leftclick(j,i):
    if b2[j][i] != NaN:  #낫띵해쁜드
        return
    
    else:
        if b2[j][i] == -2:
            # 깃발 
            return
        if 1 <= b1[j][i] and b1[j][i] <= 8:#답지 칸 번호 배열 불러오기
            b2[j][i] = b1[j][i]
            return
        if b1[j][i] == -1:
            clear = 2 
            return
        if b1[j][i] == 0:
            repeat(j,i)
            return
        return

def repeat(j,i): #좌클했는데 0일경우
    try:
        if b2[j][i] != NaN: #만약 열려있는 칸이라면 건너뜀
            return
        
        b2[j][i] = b1[j][i] #닫혀있는 칸을 열어줌

        if 1 <= b1[j][i] and b1[j][i] <= 8: #연 칸이 숫자라면 종료
            return

        for k in range(8): #0인 칸만 남으면 재귀 ㄱㄱ
            jj = j + arr[k][0]
            ii = i + arr[k][1]
            repeat(jj,ii)

    except:
        return #테두리 칸 그거 어쩌구
    return

def rightclick(): #우클
    if b2[j][i] == NaN:
        b2[j][i] = -2
        #깃발 이미지로 변경
        return
    if b2[j][i] == -2:
        b2[j][i] == NaN
        #칸 기본 이미지로 변경
        return




clear = 0
while clear == 0:
    clickButton


if clear == 1:
    print("성공")
else:
    print("유감")
#mine = -1
#flag = -2
#b1 = 답지
#b2 = 문제지
#열지 않은칸 -3
clear = 0
b2 = [[-3 for _ in range(20)] for _ in range(15)]
# col = j row = i

arr = [(-1, -1), (-1, 0), (-1, 1),( 0, -1), ( 0, 1),( 1, -1), ( 1, 0), ( 1, 1)]
#답지는 폭탄 -1과 숫자로 써져있는 완성된 배열
#풀이는 연산 시행 부분 대조한 뒤 가져오기
def leftclick(i,j):
    global clear
    if b2[i][j] != -3:  #낫띵해쁜드
        return
    
    else:
        if 1 <= b1[i][j] and b1[i][j] <= 8:#답지 칸 번호 배열 불러오기
            b2[i][j] = b1[i][j]
            return
        if b1[i][j] == -1:
            clear = 2 
            return
        if b1[i][j] == 0:
            repeat(i,j)
            return
        return

def repeat(i,j): #좌클했는데 0일경우
    try:
        if b2[i][j] != -3: #만약 열려있는 칸이라면 건너뜀
            return
        
        b2[i][j] = b1[i][j] #닫혀있는 칸을 열어줌

        if 1 <= b1[i][j] and b1[i][j] <= 8: #연 칸이 숫자라면 종료
            return

        for k in range(8): #0인 칸만 남으면 재귀 ㄱㄱ
            ii = i + arr[k][0]
            jj = j + arr[k][1]
            repeat(ii,jj)

    except:
        return #테두리 칸 그거 어쩌구
    return

def rightclick(i,j): #우클
    if b2[i][j] == -3:
        b2[i][j] = -2
        #깃발 이미지로 변경
        return
    if b2[i][j] == -2:
        b2[i][j] = -3
        #칸 기본 이미지로 변경
        return



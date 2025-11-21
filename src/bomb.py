# 폭탄 배치 
import random
import numpy as np

# None으로 가득 채운 15행 20열 2차원 넘파이 배열
bomb_Nlist2 = np.array([[None for i in range(20)]for k in range(15)])

qua1 = bomb_Nlist2[:7 , 10:20] # 1사분면 11~20열 1~7행
qua2 = bomb_Nlist2[:7 , :10] # 1~10열 1~7행
qua3 = bomb_Nlist2[7: , :10] # 1~10열 8~15행
qua4 = bomb_Nlist2[7: , 10:20] # 11~20열 8~15행

bn = 50 #폭탄의 개수는 50개

def qua_wh_all() : # 사분면 마다 폭탄을 배치하는 함수
    count1 = 0 #1사분면 count
    count2 = 0 #2사분면 count
    count3 = 0 #3사분면 count
    count4 = 0 #4사분면 count
    while count1 < 12 :  #1사분면에 폭탄 12개 배치
        x1 = random.randrange(0, 7)
        y1 = random.randrange(0, 10)
        if qua1[x1][y1] == None :
            qua1[x1][y1] = -1
            count1 += 1
    
    while count2 < 12 : #2사분면에 폭탄 12개 배치
        x2 = random.randrange(0, 7)
        y2 = random.randrange(0, 10)
        if qua2[x2][y2] == None :
            qua2[x2][y2] = -1
            count2 += 1

    while count3 < 13 : # 3사분면에 폭탄 13개 배치
        x3 = random.randrange(0, 8)
        y3 = random.randrange(0, 10)
        if qua3[x3][y3] == None :
            qua3[x3][y3] = -1
            count3 += 1

    while count4 < 13 : # 4사분면에 폭탄 13개 배치
        x4 = random.randrange(0, 8)
        y4 = random.randrange(0, 10)
        if qua4[x4][y4] == None :
            qua4[x4][y4] = -1
            count4 += 1

    return bomb_Nlist2

print(qua_wh_all())
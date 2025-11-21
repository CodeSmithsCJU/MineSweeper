# 폭탄 배치 
import random
import numpy as np

bomb_Nlist2 = np.array([[None for i in range(20)]for k in range(15)])

qua1 = bomb_Nlist2[:7 , 10:20]
qua2 = bomb_Nlist2[:7 , :10]
qua3 = bomb_Nlist2[7: , :10]
qua4 = bomb_Nlist2[7: , 10:20]

bn = 50 #폭탄의 개수는 50개

ex_bomb2 = np.array([[None for i in range(10)]for k in range(7)]) 

def qua_wh_all() :
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    while count1 < 12 :
        x1 = random.randrange(0, 7)
        y1 = random.randrange(0, 10)
        if qua1[x1][y1] == None :
            qua1[x1][y1] = -1
            count1 += 1
    
    while count2 < 12 :
        x2 = random.randrange(0, 7)
        y2 = random.randrange(0, 10)
        if qua2[x2][y2] == None :
            qua2[x2][y2] = -1
            count2 += 1

    while count3 < 13 :
        x3 = random.randrange(0, 8)
        y3 = random.randrange(0, 10)
        if qua3[x3][y3] == None :
            qua3[x3][y3] = -1
            count3 += 1

    while count4 < 13 :
        x4 = random.randrange(0, 8)
        y4 = random.randrange(0, 10)
        if qua4[x4][y4] == None :
            qua4[x4][y4] = -1
            count4 += 1

    return bomb_Nlist2

print(qua_wh_all())
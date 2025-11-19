# 폭탄 배치 
import random
import numpy as np
# [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
bomb_list = np.array([
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 1줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 2줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 3줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 4줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 5줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 6줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 7줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 8줄 
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 9줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 10줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 11줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 44, 18, 19, 20], # 12줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 13줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], # 14줄
             [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]) # 15줄

# print (bomb_list.shape)
# 사분면 = qua (quadrant 앞글자 3개)

qua1 = [bomb_list[:7 , 10:20]]
#print(bomb_list[1][2])
qua2 = [bomb_list[:7 , :10]]

qua3 = [bomb_list[7: , :10]]

qua4 = [bomb_list[7: , 10:20]] 

bn = 50 #폭탄의 개수는 50개

ex_bomb = np.array([
           [ None, None, None, None, None, None, None, None, None, None], #1줄
           [ None, 1, None, None, None, None, None, None, None, None], #2줄
           [ None, None, None, None, None, None, None, None, None, None], #3줄
           [ None, None, None, None, None, None, None, None, None, None], #4줄
           [ None, None, None, None, None, None, None, None, None, None], #5줄
           [ None, None, None, None, None, None, None, None, None, None], # 6줄
           [ None, None, None, None, None, None, None, None, None, None]]) #7줄

ex_qua1 = [ex_bomb[:4 , :6]]
#print(ex_qua1)

#ex_bomb2 = np.array ([
          # [ None, None, None, None, None, None, None, None, None, None], #1줄
          # [ None, None, None, None, None, None, None, None, None, None], #2줄
          # [ None, None, None, None, None, None, None, None, None, None], #3줄
          # [ None, None, None, None, None, None, None, None, None, None], #4줄
          # [ None, None, None, None, None, None, None, None, None, None], #5줄
          # [ None, None, None, None, None, None, None, None, None, None], #6줄
          # [ None, None, None, None, None, None, None, None, None, None], #7줄
          # [ None, None, None, None, None, None, None, None, None, None]]) #8줄

def qua1_bn() :
    for i in range(0, 13, 1) :
        x = random.randrange(0,3)
        y = random.randrange(0,5)
        if ex_qua1[x][y] == None :
            ex_qua1[x][y] = -1
    return ex_bomb

def qua2_bn() :
    for i in range(0, 13, 1) :
        x = random.randrange(0,7)
        y = random.randrange(0,10)
        if ex_bomb[x][y] == None :
            ex_bomb[x][y] = -1
    return ex_bomb

def qua3_bn() :
    for i in range(0, 14, 1) :
        x = random.randrange(0,8)
        y = random.randrange(0,10)
        if ex_bomb2[x][y] == None :
            ex_bomb2[x][y] = -1
    return ex_bomb2

def qua4_bn() :
    for i in range(0, 14, 1) :
        x = random.randrange(0, 8)
        y = random.randrange(0, 10)
        print(x,y)
        if ex_bomb2[x][y] == None :
            ex_bomb2[x][y] = -1
    return ex_bomb2

print(qua1_bn())
#print(ex_bomb2)
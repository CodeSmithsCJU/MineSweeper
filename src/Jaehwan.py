import random
i=0
n=0
lst = ["me", "you", "kim", "seong"]
print("홀짝게임 시작 1, 2중 선택")

while n < len(lst):
    r = random.randrange(1,3)
    ran = int(input("숫자 입력: "))
    if ran == r:
        print(lst[n], "is babo")
    else:
        print("you are lucky")
    n=n+1
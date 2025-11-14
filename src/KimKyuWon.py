import random
print("구구단 게임~!")
print("랜덤한 구구단이 3번 나올거에요~ 한번 자알 맞춰보세요~")
count = 0
for i in range(3):
    x = random.randrange(1,10)
    y = random.randrange(1,10)
    s = x*y
    ans = int(input(f"{x} X {y} ="))

    if ans == s:
        print("정답입니다~")
    else:
        print(f"틀렸습니다.. \n정답은:{s} 입니다..")
        count += 1

print(f"끝났습니다~ \n틀린 개수는 {count}개 입니다.")
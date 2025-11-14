import random
choices = ["가위", "주먹", "보자기"]
que = input("가위 주먹 보자기 중 하나를 입력해주세요: ")

com = random.choice(choices)
print("컴퓨터의 선택은: ",com,"이었습니다!ㅋㅋ")

if que == com :
    print("비김")
elif (que == "가위" and com == "보자기") or (que == "주먹" and com == "가위") or (que =="보자기" and com == "주먹"):
    print("당신이 이겼습니다!")
else :
    print("너가 짐 ㅋ")
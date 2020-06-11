score = int(input("점수를 입력하세요 : "))

if score <= 100 and score >= 0:
    if score > 90 and score <= 100:
        print("A학점 입니다.")
    elif score > 80 and score <= 90:
        print("B학점 입니다.")
    elif score > 70 and score <= 80:
        print("C학점 입니다.")
    else:
        print("F학점 입니다.")
else:
    print("점수를 잘 못 입력하셨습니다.")

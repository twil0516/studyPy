a = int(input("숫자를  입력해주세요.\n"))

b = 1

count = 0

hund = 0
ten = 0
one = 0


if a < 100:
    b = a
    
elif a >= 100:
    for i in range(100, (a+1)):
        hund = (i//100)
        ten = ((i%100)//10)
        one = ((i%100)%10)
        if ((hund-ten) == (ten-one)):
            count += 1
    b = (count + 99)
        
    
else:
    print("숫자가 올바르지 않습니다.\n")
print("한수의 갯수 : " + str (b) + "\n")

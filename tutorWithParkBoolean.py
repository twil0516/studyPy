# 사칙연산과 그 외의 연산자들
# 더하기 빼기 곱하기 나누기
# 제곱, 몫, 나머지

#print(10+2)
#print(10-2)
#print(10*2)
#print(10/2)

#print(10**3)
#print(10//3)
#print(10%3)

# 논리연산 그리고 or 또는

a = int(input("숫자를 입력해주세요 : "))
b = int(input("숫자를 입력해주세요 : "))

# AND 연산자

# a     b      c
# true  true   true
# true  false  false
# false true   false
# false false  false
  
#if a > 10 and b < 10:
#    print("True\n")

# OR 연산자
# a     b     c
# true  true  true
# true  false true
# false true  true
# false false false

if a > 10 or b < 10:
    print("True")
    print(a + b)


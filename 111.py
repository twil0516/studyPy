# 반복문 while 예제
# while -> 단순반복만가능
# 그래서 중첩루프 즉 이중이상 반복문을 위해 for문을 사용
# for 기본구조
# for i in range (숫자) 혹은 for i in range (숫자, 숫자)
# 0 부터 시작해서 숫자 -1 까지 반복

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end = '')
    print()









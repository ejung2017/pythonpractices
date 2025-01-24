# Day 1 questions 

# 1. 구구단표가 자동 생성되도록 프로그램을 작성하시오
for i in range(2,10): 
    for j in range(1,10): 
        print("{} x {} = {}".format(i, j, i*j))

#2. 숫자를 입력 받아 다음 결과처럼 한 행에 숫자 열을 프린트하는 프로그램을 작성하세요.
for i in range(10,0,-1): 
    print(i, end=' ')

#3. 윤년을 구하자
#윤년은 4로 나누어지고 100으로는 나누어지지 않는 해를 말한다
for year in range(2000, 2100): 
    if year % 4 == 0 and year % 100 != 0: 
        print(year, end=" ")

# 4.  숫자 n을 읽고 n보다 작은 소수를 모두 모아 리스트 형태로 프린트하고 몇개의 소수가 있는지 보여주는 프로그램을 작성하시오 
# (소수란 1과 그 자신 이외의 숫자로는 나누어 떨어지지 않는 수를 뜻함) 
number = int(input("n: "))
prime = []
for i in range(1, number+1):
    count = 0 
    for j in range(1, number+1): 
        if i % j == 0: 
            count += 1
    if count == 2: 
        prime.append(i)
print(prime)
print(len(prime))

# 5. 0-99까지 범위의 random number 50개가 있는 숫자 리스트 X를 만들고 리스트를 보여진다.
# 1) 그 중 홀수만 모아서 ODD, 짝수만모아서 EVEN리스트를 만들어 프린트하세요
import random 
x = []
even = []
odd = []

for i in range(50): 
    x.append(random.randint(0,100))
print(x)
for i in x: 
    if i % 2 == 0: 
        even.append(i)
    else: 
        odd.append(i)
print(even)
print(odd)
# 2) ODD, EVEN 리스트를 각각 sorting하여 프린트한다
even.sort()
odd.sort()
print(even)
print(odd)

# 6. 임의의 숫자를 입력받고 그 안에 소수(prime number)가 몇개 있는지 세는 프로그램을 작성하세요. (recheck)
# 소수는 1과 그 자신 외에는 나누어 떨어지지 않는 수를 말함
n = int(input("n: "))
prime_sum = 0
for i in range(1,n+1): 
    count = 0
    for j in range(1,n+1): 
        if i % j == 0: 
            count += 1
    if count == 2: 
        print(i)
        prime_sum += 1 
print(prime_sum)

# 7. 숫자 n을 읽고 N의 약수를 나열/프린트하는 프로그램을 작성한다. 이 프로그램을 while True안테나하고 무한히 반복하도록 한다.
# 즉, 숫자 n읽는 과정이 계속 반복된다.
# 단, n이 음성이면 loop를 빠져나오도록한다

while True: 
    n = int(input("n: "))
    divisors = []
    if n >= 0: 
        for i in range(1,n+1): 
            if n % i == 0: 
                divisors.append(i)
        print(divisors)
    else: 
        break



# 8. 1000원으로 자판기 물건 하나 구매한 경우 거스름돈을 계산하여 프린트 하세요
# 300원인 경우 거스름돈 700원
cash = 1000
change = cash - 300 
print(change)

# 9. N의 약수 중 소수를 찾으세요 (recheck)

#  10. 1000원으로 물건을 구매한 경우 거스름동전 500원 100원 50원 10원 각각 몇개인지 계산하기
# (최대한 큰 금액 동전으로 거스름돈을 주어야 한다)

# 11. 100000초는 몇 일, 몇 시간, 몇 분, 몇 초인지 계산하기

# 12. 숫자 n을 읽고 n보다 작은 짝수 전체의 합과 n보다 작은 홀수 전체의 합을 구해서 2개의 숫자를 프린트하세요

# 13. 임의의 두 수 n, m을 읽고 두수의 최대공약수를 계산하는 프로그램을 작성하시오. 두수의 공통약수는 몇개인지도 계산하여 프린트하시오. 

# 14. 다음 리스트 X는 중복된 원소가 있다. set 연산을 사용하지 않고, loop를 이용, X의 중복을 제거하여 newlist에 저장하는 프로그램을 작성하시오.

# 15.  두사람 X, Y는 다트게임을 하고 있다. 20회 반복해서 얻는 점수는 실제 측정하는 대신, randint()함수를 이용하여 주어진다고 가정한다. X 점수, Y점수 형태가 각 trial 별로 주어졌을때, 전체 데이터에 대한 통계 자료를 정리하고자 한다.
# 1) X가 얻은 최저, 최고 점수, Y가 얻은 최저, 최고 점수를 보여라.

# 2) 20회 동안 X의 평균점수, Y의 평균 점수를 보여라

# 3) 매 trial 별로 점수가 높은 사람이 이기는 것으로 할 때, X가 Y에게 몇 회 이겼는지 계산하여 보여라

# 4) 20회 전체에 대해서 X의 승률, Y의 승률을 보여라 (승률 = 이긴횟수/게임수)
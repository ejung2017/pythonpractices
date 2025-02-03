# Day 2 practice

## 문제1)
# 다음은 addone 함수를 정의한 다음, map함수를 이용하여 addon함수를 리스트 각 element에 적용하는 예를 보여준다.
# 이 map 함수 사용법을 이용하여 리스트 x의 각 원소별로 10으로 나눈 나머지를 계산하여 리스트로 저장하도록 하여라 (반드시 map 이용)
def addone(n):
	return n%10 

x = [10, 20, 30, 40, 51]

#1
map1 = map(addone, x)
print(list(map1))

#2 
map2 = list(map(lambda x: x%10, [10,20,30,40,51]))
print(map2)

## 문제2)
# 1에서 100까지의 난수 10개를 얻어서 정렬하시오. 그리고 3의 배수만을 항목으로 구성된 리스트를 만들어 다음과 같이 출력하는 프로그램을 작성하시오

## 문제3)
# 임의의 두수 n,m을 읽고, 두수 사이에 0.5간격으로 값을 리스트로 만들어 프린트하는 프로그램을 작성하시오, n이 m보다 작다고 가정해도 좋음. 특수함수는 사용하지 않고, 반드시 while또는 for를 이용해야함
# 간격이 0.5가 아닌 0.2 또는 0.1등 다른 실수 값도 작동해야함
"""
Two numbers:16 18
16 18
[16.0, 16.5, 17.0, 17.5, 18.0]
"""
# Assume m > n 
n = float(input("n: "))
m = float(input("m: "))
#for loop
count = int((m-n)*2)
lst = [n]
for i in range(count): 
	n += 0.5 
	lst.append(n)
print(lst)

n = float(input("n: "))
m = float(input("m: "))
#while loop
lst2 = [n]
while n<m:
	n += 0.5 
	lst2.append(n) 
print(lst2)


## 문제4)
# 다음과 같이 중첩된 리스트가 있을때, 다음과 같이 출력하는 프로그램을 작성하세요. m에 주어진 원소가 무엇인지, 원소개수가 몇개인지 모른다고 가정하여 while 또는 for loop을 사용하여 해결해야함
m = [[1,2],[3,4],[5,6],[7,8]]
"""
결과
1 2 
3 4 
5 6 
7 8 
1 3 5 7
2 4 6 8
"""
for list_element in m: 
	print(' '.join(map(str,list_element)))

for index in range(len(m[0])): 
	print(' '.join([str(i[index]) for i in m]))
	
## 문제5)
# 다음 리스트 X는 중복된 원소가 있다. set 연산을 사용하지 않고, loop를 이용, X의 중복을 제거하여 newlist에 저장하는 프로그램을 작성하시오.
X = ['A','B','C','D','B','D','E']
new_list = []

for letter in X: 
	if letter not in new_list: 
		new_list.append(letter)
print(new_list)

## 문제 6)
# 다음 3개의 리스트 X,Y,Z가 주어졌을때, X에는 속하지만, Y에는 속하지 않으면서, Z에 속하는 원소를 모두모아서 newlist에 저장하려고 한다. 
# 해당 원소 모음을 만들어 프린트하시오. 단 set함수를 사용하면 안되고, for loop을 사용하여 해결하시오
X = ['A','B','C','D','N','U','E']
Y = ['A','H','C','D','K','G','F']
Z = ['A','U','E','D','K','N','U']

## 문제 7)

# 다음 주어진 데이터는 각 사람별로 성적(중간, 기말), 자녀수, 공부시간수, 지역에 대한 정보이다. 
# 계속 임의의 사람에 대한 데이턱가 주어질 예정이니, loop 프로그램을 이용하여 해결해야함. 수동으로 계산해서 찾지 않고, 자동화해야함.
    # 1) 중간, 기말 성적 함이 가장 큰 사람을 찾고, 그 사람이름, 자녀수, 공부시간을 프린트하시오

    # 2) 자녀 수가 1인 사람 모두 찾아서 그사람의 이름, 사는 지역, 성적, 공부시간을 보여라.
score = {'Lee': [90,85],'Kim':[45,96],'Park':[53,89]}
child = {'Lee':1,'Kim':1,'Park':3}
hours = {'Lee':1000,'Kim':200,'Park':300}
area = {'Lee':'loc A','Kim':'loc B','Park':'loc A'}

#1 
score_sum = [(k, sum(score[k])) for k in score.keys()]
score_sum = sorted(score_sum, key=lambda x:x[1], reverse=True) #[('Lee', 175), ('Park', 142), ('Kim', 141)]
highest_scorer = score_sum[0][0] #Lee 
print(highest_scorer, child[highest_scorer], hours[highest_scorer]) # Lee 1 1000

#2 
for name in child.keys(): 
	if child[name] == 1: 
		print(name, area[name], score[name], hours[name])

# Lee loc A [90, 85] 1000
# Kim loc B [45, 96] 200

## 문제 8)
# 두사람 X, Y는 다트게임을 하고 있다. 20회 반복해서 얻는 점수는 실제 측정하는 대신, randint()함수를 이용하여 주어진다고 가정한다. 
# X 점수, Y점수 형태가 각 trial 별로 주어졌을때, 전체 데이터에 대한 통계 자료를 정리하고자 한다.
    # 1) X가 얻은 최저, 최고 점수, Y가 얻은 최저, 최고 점수를 보여라.

    # 2) 20회 동안 X의 평균점수, Y의 평균 점수를 보여라

    # 3) 매 trial 별로 점수가 높은 사람이 이기는 것으로 할 때, X가 Y에게 몇 회 이겼는지 계산하여 보여라

    # 4) 20회 전체에 대해서 X의 승률, Y의 승률을 보여라 (승률 = 이긴횟수/게임수)

from random import randint
for k in range(20):
	a = randint(0,100)
	b = randint(0,100)
[k,a,b]

## 문제 9)

# 0에서 9까지의 한자리 숫자를 임의로 4개 지정하여 리스트로 만든다. 그리고 사용자가 4개의 숫자를 모두 맞출 때까지 게임을 진행한다.

# 아래에 나온 것처럼 interactive mode로 게임은 진행되고 숫자를 맞추거나 못 맞출 때마다 그에 따른 메시지를 보여준다. 현재까지 맞춘 숫자리스트도 보여준다. 이 게임 프로그램을 작성하시오
"""
Guess 4 digits
- - - -
3
Cannot find it
- - - -
5
Cannot find it
- - - -
0
Yes. 0 is in the pool
0 - - -
7
Yes. 7 is in the pool
0 7 - -
8
Yes. 8 is in the pool
0 7 8 -
6
Yes. 6 is in the pool
0 7 8 6
All digits are found. Game is over.
"""
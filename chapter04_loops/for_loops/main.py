'''
1. for 반복문의 기본 개념:
     정해진 구간 혹은 집합 내의 요소들을 순서대로 꺼내면서 반복작업 수행.
     예를 들어 아까 전에 문자열의 index 개념을 학습했습니다.
     string의 경우 문자열의 문자 개수만큼 반복이 진행된다고 해석할 수 있습니다.
     collection을 기반으로 반복문을 배울수도 있지만 이건 다음 시간에.

        1) 숫자 범위를 이용한 반복
            range(): 몇 번 반복할 것인가를 지정하는 함수.
'''
from pstats import count_calls

# n=1
# while n<11:
#     print(n)
#     n+=1
#
# #1부터 10까지를 출력하는 for 반복문
# for i in range(11):
#     print(i)
#
# print()
#
# for i in range(10):                  #반복횟수는 10번, 시작점이 0
#     print(i+1)

'''
        range()함수의 응용:
            range( (시작값), 종료값, (증감값))
            
            시작값: 생략 가능, 생략 시 0부터 시잗.
            종료값: 명시 x 끝까지 진행
            증감값: 생략 가능, 생략 시 1씩 증가
        
for 반복문
형식:
for i(아무거나 사용가능) in range (시작값, 종료값, 증감값):
'''

# for i in range(1, 10, 1):               # 종료값이 10인데 1부터 시작, 9까지 나타남
#     print(i)

'''
    2) 문자열을 이용한 반복
         문자열의 경우 []를 통해 내부에 인덱스 넘버를 명시할 수 있다는 것을 확인했습니다.
         그래서 in range()를 사용하는 방법 및 향상된 for문을 사용하는 방법을 통해 
         문자를 하나씩 추출할 수 있습니다.
'''

name="Hansehyeon"
# for i in range(len(name)):      #len(): ()안에 들어가는 요소의 길이를 반환하는 함수
#     print(name[i])
#
# print(len(name))

# enhanced for loop
# for letter in name: #name이라는 string에서 각 문자 하나씩을 뽑아 letter에 대입함.
#     print(letter)
#
# # 첫 번재 반복의 경우
# letter=name[0]
# print(letter)
# #두 번재 반복
# letter=name[1]
# print(letter)
# ...
# letter=name[8]
# print(letter)

'''
대부분의 경우 반복문을 사용하게 되면 반복 대상이 되는 객체는 복수형의 변수명을 지닌다.
예) numbers=[1,2,3,4,5]

for number in numbers:
    print(number)

향상된 for loop의 형식:
for 변수 in 반복대상객체:
    반복 실행문
    
반복대상객체(iterable): 내부에 요소가 다수 들어가있어 반복적으로 요소의 데이터를 다룰 수 있는 객체 
예) str, list, tuple, set, dict

주의사항:
    if 조건문과 같이 들여쓰기
    
문자열에서 특정 문자의 개수 세기
'''

# count_a=0
# count_letters=0
#
# for letter in "banana":
#     if letter=="a":
#         count_a +=1
#     print(letter)
#     count_letters +=1
# print(f"a의 개수: {count_a}")

'''
reborg's world hurdle #1

for i in range(6)       # 1칸만 올라가는 경우
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    
#2
n=0
while n<6
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    n+=1
    
#3
def turn_right():
    for _ in range(3):
        turn_left()
        
for _ in range(6):      #6번 반복
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    for _ in range(3):      # turn_left 3번 반복.
        turn_left()
#4        
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for _ in range(6):    
jump()    

#5
def turn_right():
    for _ in range(3):
        turn_left()
        
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()    
    
    
#6
def turn_right():               # turn_right 함수
    for _ in range(3):
        turn_left()
        
def jump():                     # jump() 함수
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    
    if front_is_clear():
        move()
    else:
        jump()
        
#7(Hudle 4)
def turn_right():
    for _ in range(3):
        turn_left()
        
def jump():        #한 칸의 장애물을 넘을 수 있음
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    
    if front_is_clear():
        move()
    else:
        jump()        


hurdle 1~4, maze까지 적용 가능한 코드(우수법)        

def turn_right():
    for _ in range(3):
        turn_left()
        
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()        
        '''



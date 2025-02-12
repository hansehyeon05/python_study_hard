import random

word_list =["apple","banana", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1: 비어있는 list인 display를 만드세요
# chosen_word의 각 문자 개수마다 "_"를 추가하세요. chosen_word =="apple"이라면,
# display = ["_", "_", "_", "_", "_"]이 되어야한다.

display_list=[]
#일반 for문
for _ in range(len(chosen_word)):
    display_list.append("_")

print(display_list)

# 향상된 for문
for letter in chosen_word:
    display_list.append("_")

print(display_list)

#todo - 2: chosen_word의 각 문자들을 반복시키세요.
# 만약 그 위치의 문자가 guess와 일치한다면 해당 위치의 display에서 해당 문자를 공개하세요.
# 예) 사용자가 "p"를 입력했고 chosen_word가 "apple"이라면 display = [ '_','p', 'p', '_', '_']

#힌트: list의 각 요쇼를 재대입
# numbers =[1,2,3,4,5]
# print(numbers)
# numbers[0]=100
# print(numbers)
guess=input("알파벳 입력하세요.>>>").lower()
for i in range(len(chosen_word)):
    if chosen_word[i]== guess:
        display_list[i]= guess

print(display_list)


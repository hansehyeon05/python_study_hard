import random   # 특정 모듈을 사용한다는 것을 맨 처음에 명시합니다.

'''
"".join(반복가능객체) method : . 앞에 있는 문자열을 기준으로 반복가능객체 요소들을 합쳐서 str으로 반환.


'''
# temp = ["안", "녕", "하", "세", "요"]
# hello = "".join(temp)
# print(hello)
# print("/".join(temp))
# print(" ".join(temp))

word_list=["apple", "banana", "camel"]
chosen_word=random.choice(word_list)

display=[]
# todo - 1: "_"가 적용된 display를 구현하세요.

#todo -2: 사용자가 추측을 반복할 수 있도록 while 반목문을 작성하세요.
# 사용자가 chosen_word의 모든 문자열들을 맞췄을 때,
# 즉, display에 더이상 "_"가 없을 떄 반복문이 멈추도록 작성.

for letter in chosen_word:
    display.append("_")
print(display)

while "_" in display:
    guess = input("알파벳 입력하세요.>>>").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)


print(" ".join(display))
print("정답입니다.")




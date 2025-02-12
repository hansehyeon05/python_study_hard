import random

stages = [''' +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=["apple", "banana", "camel"]
chosen_word=random.choice(word_list)

display=[]
for letter in chosen_word:
    display.append("_")
print(display)

end_of_game = False
lives=6

while not end_of_game:
    guess = input("알파벳 입력하세요.>>>").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        # 틀렸을 떄 사용될 조건문
        # else:
        #     lives-=1
        #     print(f"당신의 기회는 {lives}번 남았습니다.")
        #     if lives==0:
        #         print("모든 기회를 잃었습니다.")
        #         break
        #         end_of_game = True
        #라고 작성하면 안된다.
        #확인하는 조건문이 실행되기 때문
        # for문 바깥에서 guess가 chosen_word에 속하지 않는지를 확인하는 조건문 작성해야 함.

    if guess not in chosen_word:
        lives -= 1

        print(f"당신의 기회는 {lives}번 남았습니다.")

        if lives== 0:
            print("모든 기회를 잃었습니다.")
            end_of_game = True
            print(f"정답은 {chosen_word}입니다.")

    if "_" not in display:
        print("정답입니다.")
        end_of_game = True
        break



print(" ".join(display))
print(stages[lives])

# 여기까지 작성했을 때 비어있는 점
# 1. 로고
# 2. word_list가 부족하다.
# 3. 테스트 해보고 유지 보수 및 리팩토링 지점이 있는지 확인할 필요가 있음.





#todo - 1 : 남은 목숨 수를 추적하기 위한 'lives'라는 변수를 선언하고, 6으로 초기화하세요.
#todo - 2 : 추측한 알파벳이 chosen_word에 없으면 lives를 1 감소시키세요.
#  lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.

#todo - 3 : display list의 모든 요소를 결합하여 문자열로 변환하세요.

#todo - 4 : 사용자가 모든 문자를 맞췄는지 확인하세요 -> 정답을 맞췄다면 "정답입니다!!:)"를 출력하세요


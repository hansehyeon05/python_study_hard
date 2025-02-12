'''
컬렉션(collection): 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나 하나를 줄로 묶어서 문자열로 출력하는데,
예를 들어 '다수의 다른 string을 관리하는 방법은 무엇일까>?

여러 명의 프로필을 관리한다고 가정.

'''
# angeunsu = "이름: 안근수\n나이 : 38\n직업: 파이썬 강사"
# print(angeunsu)
# kimrandom = "이름: 김랜덤\n나이: 20\n직업: 학생"
# print(kimrandom)

'''

종류:
    1. list 리스트 : 추가/ 수정/ 삭제가 언제나 가능/ a=[1,2,3]
    2. tuple : 추가/ 수정/ 삭제가 불가능/ a=(1,2,3)
    3. set : 중복된 값의 저장이 불가능 / a={1,2,3}
    4. dict : 키+값으로 관리 / a{ "name: "안근수", "age": 38}
    
1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 라스트에 저장 가능.
    하나의 배열에 동일한 자료형만을 저장할 수 있는 파이썬의 장점.
    '''
# li=[ 1,2,3, "한세현"]
# print(li)
'''
    1-1. list의 index와 slice
        list는 str과 동일한 방식의 index와 slicing을 지원함.
        1) 인덱스와 마이너스 인덱스
'''

# print(li[0])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[-1])
# print(li[-2])
...
'''
    2) slice
    str의 슬라이싱과 같이 '시작 인덱스: 종료 인덱스: 증감값'으로 이루어져 있음.
'''

# list_num1=[100, 3.14, "hello"]
# list_num2=list([4,5,6,7,8,9])
# print(list_num1)
# print(list_num2[0:4:2])
'''
        3) list요소의 추가와 삭제
        list에 새로운 요소를 추가할 때는 .append()와 .insert() '메서드'를 사용할 수 있다.
        기존 요소를 삭제할 때 에는 .pop() 메서드를 사용한다.
        
        .append() - 항상 마지막 인덱스에 요소를 추가하는 메서드
        .insert(위치,값) - 정해진 위치에 해당 값을 추가하는 메서드
'''
# scores=[30,40,50]       #scores라는 list 내에 있는 int데이터인 30,40,50
#                         #요소라고 한다
#                         # 함수와 달리 list명.메서드명의 형태로 사용했다->> 호출 방식이 다르다
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0,90)
# print(scores)
# '''
#         pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됨.
#         pop(인덱스넘버)로 잓성하면 해당 인덱스의 요소를 삭제함.
# '''
# scores.pop()
# print(scores)
# scores.pop(0)   # 오버로딩의 기초 개념이 포함돼 있어서 동일한 메서드명인데도 arguement가 있을 수도 있음
# print(scores)
'''
교재에 없는 삭제 메서드: .remove(값)을 사용하면 list 내에 해당 값을 찾아 삭제.
# '''
# scores.remove(40)
# print(scores)
# # 이상의 코드까지 실행시켯 을때 인덱스가 두개 밖에 없어서 10개 정도의 요소 추가
#
# for i in range(10):
#     scores.append(i*10)
#
# print(scores)
#
#
# # list 내의 요쇼들을 하나씩 뽑아내는 반복문- for문->
#
# for i in range(len(scores)):
#     print(scores[i])
#
# # 향상된 for문 사용-> 읽기만 가능
# for score in scores:        # 전에 말했던 것처럼 collections의 경우 복수로 이름 짓고
#                             # 향상된 for문에서 각 변수는 단수로 이름 짓는 경우가 많다.
#     print(score)
'''
    2. tuple() : 저장된 값을 변경할 수 없는 list라고 생각하시면 됩니다. 인덱스와 슬라이스를 
    사용하지만 저장된 값 이외에는 추가/수정/삭제가 불가능.
    
    튜플은 소괄호를 통해 생성
'''
# tuple_num1= (1,2,3)
# tuple_num2= tuple((4,5,6))
# tuple_num3= 7,8,9
# print(tuple_num1)
# print(tuple_num2)
# print(tuple_num3)
# # 복수의 변수 선언 및 초기화 방법
# a,b,c=7,8,9
# print(a)
# print(b)
# print(c)
# '''
#
#         튜플 생성 방법 3을 이용한다고 가정했을 때, 값이 하나 밖에 없는 튜플을 생성한다면
#         tuple_num4=0이라고 입력할 경우 생길수 있는 문제?
# '''
# tuple_num4=0
# print(tuple_num4)
# print(type(tuple_num4))
# tuple_num5=0,
# print(tuple_num5)
# print(type(tuple_num5))
'''
    1) 튜플에서의 인덱스/ 마이너스 인덱스 
'''
# tuple_num6= 1,2,3,4,5,6,7,8,9,10
# print(type(tuple_num6[2]))  #collections의 element에 type() 함수를 적용하면,
#                             # element의 자료형이 반환
#                             # 즉, tuple_num6[2]는 3이라는 element를 가리키기 때문
#                             # type() 함수 적용 시 <class 'int'>로 출력됨.
# tuple_num7= "hello.", "nice to meet you", "myname is", "hansehyeon", "I am", "21", "years old."
#
# for words in tuple_num7:
#                                 #str의 메서드.upper()는 str을 대문자로 바꿔주는데, 안먹힌 이유는?
#     print(words.title(), end="")        #튜플의 정의 생각.
#
# for words in tuple_num7:
#     print(words, end="")
#
# str_example= "hansehyeon"
#
# print(str_example.upper())
# # '''
#     3. set
#         수학의 집합 개념을 구현한 자료형. list와의 차이점은 순서가 없기 때문에 인덱스 및 슬라이싱
#         사용이 불가능. 중복된 값의 저장이 불가능.
#
#         이를 활용하여 중복 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우 사옹.
#
#         set를 사용하기 위해서는 중괄호 사용
'''
set_num1={1,2,3}
set_num2= set({4,5,6})
print(set_num1)
print(set_num2)

li=[]
tu=()
se={}

print(type(li))
print(type(tu))
print(type(se))'''
'''
    se={} 형태로 비어있는 set를 생성했을 경우 se는 사실 <class 'dict'> 이기 때문에 
    비어있는 set를 만들기 위해서는 세트 생성 방법 2를 사용해야 함.
'''
#se = set({})
# print(type(se2))
'''
    특징:
        1. 저장돠는 순서가 없다.
        2. 중복되는 값을 저장 불가능
        3. list와 연계해서 많이 쓰임
'''
# list_num5= [1,1,2,2,3,3]
# print(list_num5)
# set_num5 = set(list_num5)
#
# print(set_num5)
# list_num6= list(set_num5)
# print(list_num6)
# '''
#     set에서는 인덱싱/ 마이너스 인덱싱/ 슬라이싱을 지원하지 않기 때문에 특정 요소만 추출하기 위해서는
#     형변환 과정이 필요함
#
#     요소 관련 메서드
#         .add()- set에 새로운 요소 추가
#         .remove()- 기존 요소를 삭제할 때
#         .discord()- 기존 요소를 삭제할 때
# '''
# set_num6= {10,20,30}
# set_num6.add(50)
# print(set_num6)
# set_num6.remove(50)
# print(set_num6)
#
# set_num6.discord(70)
'''
    4. dictionary- 말 그대로 사전의 의미를 생각하면 된다. 종이 사전을 찾아보게 되면 
     flower: 꽃
     dictionary: 사전
     으로 기재되어있다. 즉 ":"을 기준으로 좌측과 우측이 나누어진 형태를 가지고 있는데
     딕셔너라는 리스트, 튜플, 세트와 달리 
     key: value의 구성으로 이루어져있다.
'''
# dict_num1={
#     "이름": "한세현"
#     "나이": 21,
#     "주소": "부산광역사"
# }
# 맨 마지막에 있는 ,의 의미는 혹시 후에 key-value를 추가할 때 이전 라인에서 콤마 입력,엔터
'''
    딕셔너리는 인덱스는 존재하지 않지만 위와 같이 KEY를 인덱스와 유사하게 사용함.
    즉, key 값을 알면 저장된 값을 확인할 수 있는 구조.
'''

#list의 각 요소를 추출하기 위한 반복문
# li2 = [10,20,30,40]
# for num in li2:
#     print(num)
# # for i in range(len(dict_num1)):
# #   print(dict_num1)
#
# for key in dict_num1:
#     print(key)
#     print(dict_num1[k])
#     print()
#
# # key 목록을 추출하는 메서드
# print(dict_num1.keys())
# print(dict_num1.values())
#
# print(type(dict_num1.keys()))
# print(type(dict_num1.values()))
#
# keys= list(dict_num1.keys())
# values= list(dict_num1.values())
#
# print(keys[1])
# print(values[2])
# '''
#     1) 딕셔너리 요소의 추가와 삭제
# '''
# dict_num1["직업"]="코리아it아카데미 파이썬 강사"
# print(dict_num1)
# dict_num1["직업"]="코리아it아카데미 웹 개발 강사"
# print(dict_num1)
#
# dict_num1.pop("직업") # key를 정확하게 입력해야 신청 가능.
# print(dict_num1)        #key를 삭제하면 value도 같이 날아간다.

'''
응용 예제)

list [10,20,30,40,50,60,70,80,90,100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그 
list에서 2번째 요소를 출력하는 프로그램을 작성하시오.

예)
3번째 요소로부터 7번째 요소 = [30,40,50,60,70]
3번째 요소로부터 7번째 요소 중 2번째 요소=40
# '''
# list_origin = [10,20,30,40,50,60,70,80,90,100]
# print(f"3번재 요소로부터 7번째 요소= {list_origin[2:7:1]}")
# print(f"3번째 요소로부터 7번째 요소 중 2번재 요소= {list_origin[2:7:1][1]}")
#
# list_sliced=list_origin[2:7:1]
# print(f"3번재 요소로부터 7번째 요소= {list_sliced}")
# print(f"3번재 요소로부터 7번째 요소 중 2번째 요소= {list_sliced[1]}")
#
'''
사용자로부터 1에서 12사이의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오.

예)
1~12사이의 월을 입력하세요 >>>2
2월은 28일 까지 입니다.
'''
# month= input("1~12 사이의 월을 입력하세요 >>>")
#
# month_int=int(month)
#
# last_dates=[31,28,31,30,31,30,31,31,30,31,30,31]
#
# print(f"{month_int}월은 {last_dates[month_int-1]}까지 있습니다.")
#
# last_date_short= [28,30,31]

# last_date_dict={
#     "1":31,
#     "2":28,
#     "3":31,
#     "4":30,
#     "5":31,
#     "6":30,
#     "7":31,
#     "8":31,
#     "9":30,
#     "10":31,
#     "11":30,
#     "12":31,
#
# print(f"{month}월은 {last_date_dict[month]}까지 있습니다.")
# }

# last_dates_short = [28,30,31]
#
# if month_int ==2:
#     last_date = last_dates_short[0]
# elif month_int ==4 or month_int ==6 or month_int ==9 or month_int ==11:
#     last_date = last_dates_short[1]
# elif month_int in (1,3,5,7,8,10,12):        #in 뒤에 collections 중에 하나가 오면 됨 (),set{}, []
#     last_date = last_dates_short[2]
# else:
#     print("잘못입력하셨습니다.")
#     last_date="x"
#
# print(f"{month}월은 {last_date}일까지 있습니다.")

'''
수학 여행을 어디로 갈지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

예)

희망하는 수학 여행지를 입력하세요>>>제주
희망하는 수학 여행지를 입력하세요>>>제주
희망하는 수학 여행지를 입력하세요>>> 민속촌

조사된 수학 여행지는 {'제주, '민속촌'} 입니다.
조사된 수학 여행지는 ['제주, '민속촌'] 입니다.
'''


# math_place_list
# for i in range(3):
#     student=input("희망하는 수학 여행지를 입력하세요>>>")
#     math_place_list.append(student)
#
# math_place_set=set(math_place_list)
# math_place_set=set(math_place_list)
# print(f"조사된 수학여행지는 {math_place_list}입니다.")

'''
짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고 그 정수만큼 숫자를 입력 받아 list에 저장.
저장된 숫자 중 짝수만 새로운 list에 저장해 출력.

예)
몇 개의 숫자를 입력할까요?>>>5
1번째 숫자를 입력하세요 >>>10
2번째 숫자를 입력하세요 >>> 15
3번째 슷자를 입력하세요 >>>20
4번째 슷자를 입력하세요 >>>25
5번째 슷자를 입력하세요 >>>30
입력 받은 숫자는 [5,15,20,25,30]입니다.
입력 받은 숫자들 중 짝수는 [10,20,30]입니다.
'''

# li_original=[]
# index_num=int(input("몇 개의 숫자를 입력할까요?>>>"))
# for i in range(index_num):
#     num=int(input(f"{i+1}번째 숫자를 입력하세요 >>>"))
#     li_original.append(num)
# li_even=[]
# print(f"입력 받은 숫자는 {li_original}입니다.")
#
# #향상된 for문
# for num in li_original:
#     if num % 2==0:
#         li_even.append(num)
#
# print(f"입력 받은 숫자는 {li_even}입니다.")

# li_original2=[]
# li_even2=[]
# for i in range(int(input(" 몇 개의 숫자를 입력하겠습니까?>>>"))):
#     num2 = int(input(f"{i+1}번째 숫자를 입력하세요 >>>"))
#     li_original2.append(num2)
#     if num2 %2 ==0:
#         li_even2.append(num2)

'''
딕셔너리 기반의 연락처 관리

사용자로부터 3명의 이름과 전화번호를 입력받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는 
프로그램 작성.

예)
1번째 사람의 이름을 입력하세요 >>>
1번째 사람의 연락처를 입력하세요 >>>
2번째 사람의 이름을 입력하세요 >>>
2번째 사람의 연락처를 입력하세요 >>>
3번째 사람의 이름을 입력하세요 >>>
3번째 사람의 연락처를 입력하세요 >>>

입력 받은 연락처는 {'김일': '010-1234-5678', '김이': '010-2345-6789', '김삼': 010-3456-7890'}입니다.
'''
# telephone={}
# for i in range(3):
#     dict_key=input(f"{i+1}번째 사람의 이름을 입력하세요 >>>")
#     dict_value=input(f"{i+1}번째 사람의 연락처를 입력하세요 >>>")
#
#     #딕셔너리에 element를 추가하는 방법
#
#     telephone[dict_key]= dict_value
# print(f"입력 빋은 연락처는 {telephone}입니다.")

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기 
문제: 비어있는 list01을 선언하고 그 안에 입력받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수: 정수n

함수 호출 
add_numbers(last_num)
print(add_numbers2(last_num))
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
'''

# def add_numbers(n):
#     list01=[]
#     for i in range(n):
#         list01.append(i+1)
#     print(list01)
#
# def add_numbers2(n):
#     list02=[]
#     for i in range(n):
#         list02.append(i+1)
#     return list02
#
#
# #함수 호출
# last_num=int(input("숫자 몇 까지 입력하시겠습니까?>>>"))
# add_numbers(last_num)
# print(add_numbers2(last_num))
#
# for number in add_numbers(last_num):
#     print(number+1)

'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의 
함수 이름: count_even_odd
매개 변수: list numbers(요소는 모두 정수일 것)

함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10])

예)
짝수의 개수:5
홀수의 개수:5

'''
# def count_even_odd(numbers):
#     even_count=0
#     odd_count=0
#
#
#
#
#
# count_even_odd([1,2,3,4,5,6,7,8,9,10])

#기본적으로 실행 단계가 작동하는지 확인

# even_count=0
# odd_count=0
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# # 반복문 돌리고 거기 내부에 조건문 돌려서 짝수면 even_count에 1씩 더하고,
# # 아니면 odd_count에 1씩 더하기
#
# def count_even_odd(numbers):
#     even_count = 0
#     odd_count = 0
#     for number in numbers:
#         if number %2 ==0:
#             even_count +=1
#         else:
#             odd_count +=1
#
#     print(f"짝수의 개수: {even_count}\n홀수의 개수: {odd_count}")
#
# count_even_odd([1,2,3,4,5,6,7,8,9,10])












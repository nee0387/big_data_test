# def add(a, b):
#     return a + b
#
#
#
# # return이 있는 함수는 변수에 넣어줘야함.
#
# def add2(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
#
# x = add(3, 4)
# x2 = add2(10, 20)
#
# print(x)
# print(x2)
#
# # return이 없으면 함수 실행 후 반환되는 값이 없음
#
# print(type(x))
# print(type(x2)) # <- 빈값이기 때문에 NoneType 출력.
#
#
#
#
# def add_many(*args): # -> 입력한 모든 값이 튜플형태로 저장
#     result = 0
#     for i in args:
#         result = result+i
#     return result
#
# x = add_many(1,2,3,4,5,6)
# print(x)
#
# # return은 조건마다 쓸 수 있지만 한번만 사용. return을 만나면 바로 탈출
# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#         return result
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#         return result
#     elif choice == "sub":
#         result =
#         for i in args:
#             result = result - i
#         return result
#     elif choice == "div":
#         result =
#         for i in args:
#             result = result / i
#         return result
#     else:
#         return "없는 연산이다."
#
# * (별 하나)는 튜플형태로 저장 *args => 값들을 모아서 튜플로 만듦
# ** (별 두개)는 딕셔너리로 저장 **args => 값들을 모아서 딕셔너리로 만듦
# *이 찍힌 매개변수들은 여러 값이 들어감.

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

def add_and_mul(a,b):
    return a+b, a*b


result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)


def mix(a,b):
    수행문1
    수행문2
    if x != 0:
        return

# 초기값을 줄 것은 가장 뒤에 위치.
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, False)



a = 1 # 전역변수
def vartest(a): # 매개변수
    a = a + 1 # 함수 안에 있는 a는 전역변수와 무관한 함수의 a

vartest(a) # 재료 a 전역변수. return하지 않았으므로. return 하면 2 출력.
print(a) # 여기의 a는 전역변수 a


total = 5000 # 전역변수

def add(ma):
    global total # 함수 안에서 전역변수 조회. 변경

    total += ma
    return total

add(3000)
print(total)


a = 1 # 전역변수 a global var

#########################################################
def vartest(a): # 매개변수 a
    a = a + 1 # 매개변수 a, 매개변수 a
    return a # 매개변수 a // 함수 안에서의 변수 // 함수변수
#########################################################

a = vartest(a) # 전역변수 a, 함수의 재료로 쓰인 인수. 전역변수 a
print(a) # 전역변수 a
#1~8 a 각각 어떤 a 인지

# 1. 함수의 구동 결과 리턴을 return 밖에 나와서 특정 변수에 넣어주는 방법
# 2. 함수 안에서 글로벌 전역변수 직접 변경해주는 방법 global
#
# 함수
# 공통된 작업에 적용가능
# 매개변수 존재
# 매개변수에 어떤 재료가 들어가냐에 따라 결과값이 다름.

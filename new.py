# # f = open("새파일.txt", 'w')
# # f.close()
#
# f = open("test1.txt", 'w', encoding='utf-8')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" %i
#     f. write(data)
#
# f.close()
#
#
# f = open("hi.txt", 'r')
# line = f.readline()
# print(line)
# f.close()
#
# f = open("hi.txt", 'r')
#
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f. close()

# f = open("hi.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# f = open("hi.txt", 'r')
# data = f.read()
# print(data)
# f.close()


# f = open("hi.txt",'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#
# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")
#
# # 절차지향언어 => 클래스 개념 x
# # 객체지향언어 => 클래스 개념 o
#
# result = 0
#
# def add(num):
#     global result
#     result += num
#     return result
#
# print(add(3))
# print(add(4))
#
#
# result1 = 0
# result2 = 0
#
# def add1(num):
#     global result1
#     result1 += num
#     return result1
#
# def add2(num):
#     global result2
#     result2 += num
#     return result2
#
# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))


# class Calculator: # 2개의 메서드를 가지고 있다. => 2개의 기능이 있다. 2개의 메서드를 묶어놨다. 한 세트
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
#     def sub(self, num):
#         self.result -= num
#         return self.result
#
#
# cal1 = Calculator() # cal1이라는 객체를 생성했다. Calculator 클래스의 인스턴스가 생성됐다. cal1이라는 이름으로 Calculator의 기능을 복제
# cal2 = Calculator() # cal2리는 객체를 생성했다. Calculator 클래스의 인스턴스가 생성됐다.
# # 객체 2개 cal1, cal2. Calculator. 2개의 계산기는 각각 독립적. 서로 영향이 없음.
#
# cal3 = Calculator()
# cal4 = Calculator()
# cal5 = Calculator()
#
#
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
#
#
# print("------------------------")
# print(cal5.add(10))


# class Cookie:
#     pass # 아무기능 없이 자리만 채워주는 문법요인
#
# c1 = Cookie() # c1은 cookie클래스의 인스턴스이다. c1은 객체이다.
# c2 = Cookie()
# c3 = Cookie()
#
#
# class FourCal:
#     def add(self, num):
#         pass
#     def sub(self, num):
#         pass
#     def mul(self, num):
#         pass
#     def div(self, num):
#         pass
#
# x = 3000
# cal1 = FourCal()
# print(type(x))
# print(type(cal1))

class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second

#################################################
def setdata():
    return "111"

a = FourCal()
b = FourCal()

# setdata 클래스에 묶여있는 함수는 밖에서 접근할 수 없음.

setdata() # => 전역적 함수
FourCal.setdata() # => 클래스 안에 있는 함수. FourCal 클래스의 클래스 함수를 호출
a.setdata() # 객체 a의 함수 => a라는 객체 관련 setdata 함수 호출
b.setdata() # 객체 b의 함수 => b 객체에 setdata를 실행하겠다.

# a.append => a에 append 하겠다
# error = np.random.rand() => 큰 것부터 써줌. 라이브러리 > 모듈 > 클래스 > 함수

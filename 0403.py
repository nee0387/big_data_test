# x=0
# y=x+1
# class FourCal:
#     def setdata(self, first, second):
#         self.x = first
#         self.y = second
#         # 셋데이터 메서드
# #######################################zmffotm
# def setdata():
#     return "111"
# # 셋데이터 함수
#
# a= FourCal()
#
# #setdata
# a.setdata(5,10)
# print(a.x)
# print(a.y)
#
#
# xx=FourCal()
# xx.setdata(5,10)
# print(xx.x)
# print(xx.y)
#
# class Fourcal:
#     def setdata(self, first, second, m, n):
#         self.x1 = first
#         self.x2 = second
#         self.x3 = m
#         self.x4 = n
#         self.x_sum = m + n
#         self.x_mul = m * n
#         self.x_div = m / n
#
#
# xx=Fourcal()
# yy=Fourcal()
#
# xx.setdata(5, 10, 20, 40) # 호출: 함수를 사용한다.
# yy.setdata(1,2,3,4)



# class Fourcal:
#     def setdata(self, first, second):
#         self.x1 = first
#         self.x2 = second
#
# a = Fourcal()
# b = Fourcal()
#
# Fourcal.setdata(a,3,10) #호출하는 주체가 정해져있지 않다.
# Fourcal.setdata(b,5,8)
# #a. setdata(3,10) #호출하는 주체가 누군지 포함되어있다.
# print(a.x1)
# print(a.x2)
# print(b.x1)
# print(b.x2)


# class Fourcal:
#     def setdata(self, first, second):
#         self.x1 = first
#         self.x2 = second
#     def add(self):
#         return self.x1 + self.x2
#     def sub(self):
#         return self.x1 - self.x2
#     def mul(self):
#         return self.x1 * self.x2
#     def div(self):
#         return self.x1 / self.x2
#
#
# mycal = Fourcal()
# mycal2=Fourcal() #포칼 클래스 객체 mycal2 생성
#
# mycal.setdata(50, 10) #mycal 객체로 데이터셋 50, 10
# mycal2.setdata(200, 600) # mycal2 객체로 데이터셋 200, 600
# result_mycal = mycal.add() # mycal 객체의 add메서드 호출
# result_mycal2 = mycal2.add() # mycal2 객체의 add메서드 호출
#
#
# xx = mycal.add()
# print(xx)


# class Fourcal:
#     def add(self, first, second):
#         return first + second
#     def sub(self, first, second):
#         return first - second
#     def mul(self, first, second):
#         return first * second
#     def div(self, first, second):
#         return first / second
#
#
# mycal = Fourcal() # 객체가 생성될 때


# class FourCal:
#     def __init__(self, first, second): # __init__: 생성자 변수. 자동으로 실행
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
#
# a = FourCal(4, 10)
# print(a.first)
# print(a.second)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# class FourCal:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def cal(self, mode):
#         if mode=="add":
#             return self.x + self.y
#         elif mode=="sub":
#             return self.x - self.y
#         elif mode=="mul":
#             return self.x * self.y
#         elif mode=="div":
#             return self.x / self.y
#         else:
#             print("없는 연산이다.")
#
# a = FourCal(4, 10)
# # print(a.cal(mode="mul"))
# print(a.cal("mul"))


# class FourCal:
#     def __init__(self, x, y, mode):
#         self.x = x
#         self.y = y
#         self.mode = mode
#         if mode=="add":
#             print(self.x + self.y)
#         elif mode=="sub":
#             print(self.x - self.y)
#         elif mode=="mul":
#             print(self.x * self.y)
#         elif mode=="div":
#             print(self.x / self.y)
#         else:
#             print("없는 연산이다.")
#
# a = FourCal(4, 10, "add")


# class FourCal: # 기능이 5가지
#     def setdata(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#     def sub(self):
#         return self.x - self.y
#     def mul(self):
#         return self.x * self.y
#     def div(self):
#         return self.x / self.y
#
#
#
# class MoreFourCal(FourCal): # 기능이 5가지는 상속을 받아왔고 1가지는 추가가 되었음. 총 6가지
#     def pow(self):
#         result = self.x ** self.y
#         return result
#
#
# a = MoreFourCal() # 기존클래스를 상속받은 클래스, 객체 생성.
# a.setdata(2, 10) # 상속받은 클래스의 객체로 셋데이터 함수 호출
# print(a.div()) # 상속받은 클래스의 객체로 div함수 호출
# print(a.pow())



class Cal: # 기능이 5가지
    def setdata(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y


# class upgradeCal(Cal): # 기능이 5가지는 상속을 받아왔고 1가지는 추가가 되었음. 총 6가지
#     def pow(self):
#         result = self.x ** self.y
#         return result
#     # morefourcal
#
# a = upgradeCal()
# b = Cal()
# b.setdata(4, 0)
# print(b.div())


# class safecal(Cal): # 기능이 5가지 셋데이터 + - * /
#     def div(self):
#         return 0
#
# a = safecal()
# a.setdata(10, 3)
# print(a.div()) # 상속받아 이름을 똑같이 지으면 오버라이드. 0이 출력
#
# b = Cal()
# b.setdata(10, 3)
# print(b.div()) # 원래의 나누기가 출력


class safecal(Cal): # 기능이 5가지 셋데이터 + - * /
    def div(self):
        if self.y == 0: # 나누는 값이 0인 경우 0을 출력
            return 0
        else:
            return self.x / self.y

a = Cal()
safea = safecal()
a.setdata(10, 0)
safea.setdata(10, 0)
print(safea.div())
# print(a.div()) # ZeroDivisionError: division by zero




# class Cal: # 기능 5가지에 클래스 변수 2개
#     lastname = "김"
#     firstname = "철수"
#     def setdata(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#     def sub(self):
#         return self.x - self.y
#     def mul(self):
#         return self.x * self.y
#     def div(self):
#         return self.x / self.y


class Family:
    lastname = "김" # 클래스에 속한 변수
    firstname = "철수" # 클래스 변수

print(Family.lastname)
print((Family.firstname))

f1 = Family()
f2 = Family()
print(f1.lastname)
print(f2.lastname)
Family.lastname = "박"
print(f1.lastname )
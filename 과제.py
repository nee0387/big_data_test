# 1. 사칙연산 기능이 있는 클래스 만들기
# 2. 그 클래스로  3개의 계산기 객체 만들기
# 3. 각각의 계산기가 독립적으로 작동되도록
# 4. 계산기 3개가 총 몇 번 구동되었는지 확인



# class Cal:
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
# x = int(input('숫자: '))
# z = input('연산: ')
# y = int(input('숫자: '))
# a = Cal()
# a.setdata(x, y)
# if z == '+':
#     print(a.add())
# elif z == '-':
#     print(a.sub())
# elif z == '*':
#     print(a.mul())
# elif z == '/':
#     print(a.div())
# else:
#     print('잘못된 입력입니다.')


# e = input('계산기 선택: ')
x = int(input('숫자: '))
z = input('연산: ')
y = int(input('숫자: '))


class Cal:
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


def cal(z):
    if z == '+':
        print(e.add())
    elif z == '-':
        print(e.sub())
    elif z == '*':
        print(e.mul())
    elif z == '/':
        print(e.div())
    else:
        print('잘못된 입력입니다.')

e = Cal()
e.setdata(x, y)
cal(z)



test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

marks = [90, 25, 67, 45, 80]

number = 0
nif = 0
nel = 0

for i in marks:
    number += 1
    if i >= 60:
        nif += 1
        print("%d번 학생은 합격입니다." % number)
    else:
        nel += 1
        print("%d번 학생은 불합격입니다." % number)

print("for문 실행횟수는 %d번" % number)
print("if문 실행횟수는 %d번" % nif)
print("else문 실행횟수는 %d번" % nel)

add = 0
for i in range(1, 11):
    add += i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ") # end="" 는 줄바꿈 하지 않고 띄어쓰기.
    print('')

a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i*3)
print(result)

result = [i*3 for i in a]
print(result)

a = 50
b = 30

print(a+b)
print(a-b)
print(a*b)
print(a/b)

if a > b:
    print(a - b)
    print(a / b)
else:
    print(b - a)
    print(b / a)

x = input()
print(x)
print(type(x))
int(x)
print(x)
print(type(x))

x = int(input())
print(x)
print(type(x))

x = int(input('연산할 숫자를 입력해주세요: '))
y = int(input('연산할 숫자를 입력해주세요: '))
z = input('연산할 방법을 입력해주세요: ')

if z == '1':
    print("연산 결과: ", x + y)
elif z == '2':
    if x >= y:
        print("연산 결과: ", x - y)
    else:
        print("연산 결과: ", y - x)
elif z == '3':
    print("연산 결과: ", x * y)
elif z == '4':
    if x >= y:
        print("연산 결과: ", x / y)
    else:
        print("연산 결과: ", y / x)
else:
    print("잘못입력했습니다.")

while True:

    x = int(input('연산할 숫자를 입력해주세요: '))
    y = int(input('연산할 숫자를 입력해주세요: '))
    print("1: 더하기, 2: 빼기, 3: 곱하기, 4: 나누기, 5: 종료")
    z = input('연산할 방법을 입력해주세요: ')

    if z == '1':
        print("연산 결과: ", x + y)
    elif z == '2':
        if x >= y:
            print("연산 결과: ", x - y)
        else:
            print("연산 결과: ", y - x)
    elif z == '3':
        print("연산 결과: ", x * y)
    elif z == '4':
        if x >= y:
            print("연산 결과: ", x / y)
        else:
            print("연산 결과: ", y / x)
    elif z == '5':
        break
    else:
        print("다시입력해주세요.")



howmany = int(input("연산할 숫자 갯수: "))
list_x = []
input_a = 0
input_b = 0
input_c = 0

# 2개일 경우
if howmany == 2:
    input_a = int(input("첫번째 숫자: "))
    input_b = int(input("두번째 숫자: "))
    list_x.append(input_a)
    list_x.append(input_b)
    print(list_x)

for i in list_x:


# 3개일 경우
elif howmany == 3:
    input_a = int(input("첫번째 숫자: "))
    input_b = int(input("두번째 숫자: "))
    input_c = int(input("세번째 숫자: "))
    list_x.append(input_a)
    list_x.append(input_b)
    list_x.append(input_c)
    print(list_x)



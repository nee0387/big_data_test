"""
a=[1, 2, 3]
print(a)
print(a[0])
b=[1, 2, 3, ['a', 'b', 'c']]
print(b[-1])
print(b[3])

c = [1, 2, ['a', 'b', ['Life', 'is']]]
print(c)
print(c[2][2][0])
print(c[2][1])
print(c[2][2][0], c[2][2][1], c[2][0])

listA = [1, 2, 3, 4, 5]
print(listA[0:2])

Xarray="12345"
print(Xarray[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])

d = [4, 5, ['q', 'w', ['e'], 'r'], 9]
print(len(d))

print(str(d[0])+(str(d[1])))

print(str(d[0])+d[2][0])

a = [1, 2, 3]
a[2]=4

print(a)


aa = [1, 2, 3]
aa.append(4)
print(aa)

aaa=[1, 5, 4, 6, 3, 7, 2]
aaa.sort()
print(aaa)

aaa.reverse()
print(aaa)

aaa.insert(0, 8)
print(aaa)

aaa.remove(8)
print(aaa)


a = [1, 2, 3]
a.extend([4, 5])
print(a)
# a=12345 + b=67 -> a에 b를 붙여 a를 확장

b = [6, 7]
a.extend(b)
print(a)

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# del t3[0] 튜플은 수정 불가
print(type(t4))

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 +t2)

dic = {'name':'pay', "phone":"0119993323", "birth":"1118"}
print(dic.values())

a = {1:'a'}
a[2] ='b'
a['c'] = 3
del a['c']
print(a)
"""
'''
grade = {'pey':10, 'julliet':99}
print(grade['pey'])
print(grade['julliet'])

# 정수는 0으로 시작할 수 없음.

dic = {'name':'pay', 'phone':119993323, 'birth':'1118'}
print(dic['name'])
print(dic['phone'])

print('name' in dic)
print('email' in dic)

if 'name' in dic:
    print(dic['name'])

# 집합(set) 자료형은 중복을 허용하지 않고 순서가 없다(unordered). 인덱싱 불가
s1 = set([1, 2, 3])
print(s1)
s2 = set("hello")
print(s2)

l1 = list(s1)
print(l1)
print(l1[0])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1&s2)
print(s2.intersection(s1))
print(s1.intersection(s2))

print(s1 | s2)

print(s1.union(s2))
print(s2.union(s1))

print(s1-s2)
print(s2-s1)

print(s1.difference(s2))
print(s2.difference(s1))

lp = "24가 2210"
print(lp[-4:])

mr = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del mr[-2]
print(mr)

del mr[-2:]
print(mr)

year = "2020"
print(int(year))
'''

'''
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

if 'money' in pocket:
    print("택시 타")
elif card:
    print("택시 타")
else:
    print("걸어가")
'''
'''
pocket=['paper', 'money1', 'cellphone']
if 'money' in pocket: pass
else: print("카드 꺼내")

score = 90
if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)

m = "success" if score >= 60 else "failure"
print(m)

# while은 조건의 반복문. 조건에 도달할때까지 무한반복.

treehit = 0
while treehit < 10:
    treehit = treehit +1
    # treehit += 1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")

prompt = """
1. add
2. del
3. list
4. quit

enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
'''
'''
# 조건이 항상 참일 경우 무한 루프에 빠진다 이를 중지하기 위해 if문에 break를 넣어 준다.
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 처음으로 돌아가게 하기 위한 명령어 continue. 뒤의 코드는 무시됨.
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)
'''

tl = ['one', 'two', 'three']
for i in tl:
    print(i)


marks = [90, 25, 67, 45, 80]
number = 0
'''
for i in marks:
    number += 1
    if i >= 60:
        print("%d번 학생 합격" % number)
    else:
        print("%d번 학생 불합격" % number)
'''

# continue 뒤의 문장은 무시하고 처음으로 돌아감.

for i in marks:
    number += 1
    if i < 60:
        continue
    print("%d번 학생 합격" % number)

a = range(10)
add = 0
for i in range(1,11):
    add += i
print(add)

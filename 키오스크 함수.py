menu = ['메인1', '메인2', '음료1', '음료2', '사이드1', '사이드2']
price = [2000, 3000, 1000, 1200, 1500, 1700]

basket = []
total = 0

def menu_select(ma):
    global total
    basket.append(menu[ma-1])
    total += price[ma-1]
    print("선택한 메뉴: ", basket)
    print("총액: ", total)

while True:
    print("1. 메인1: 2000, 2. 메인2: 3000, 3. 음료1: 1000, 4. 음료2: 1200, 5. 사이드1: 1500, 6. 사이드2: 1700")
    x = int(input("메뉴를 선택하세요(1~6): "))

    for i in range(6):
        if i == x-1:
            menu_select(x)

    else:
        print("다시 입력해주세요")

    z = input("메뉴를 추가하시겠습니까[y, n]?" "\n"
              "(선택메뉴 초기화: c) ")

    if z == 'y':
        continue
    elif z == 'n':
        break
    elif z == 'c':
        # basket.clear()
        basket = []
        total = 0
        print("선택한 상품: ", basket)
        print("결제할 금액: ", total)
    else:
        print("다시입력해주세요")
        z = input("메뉴를 추가하시겠습니까[y, n]? ")
        if z == 'y':
            continue
        elif z == 'n':
            break

member = ['aaa', 'bbb', 'ccc', 'ddd']
while True:
    m = input("회원이십니까[y, n]? ")
    if m == 'y':
        id = input("아이디: ")
        if id in member:
            for i in range(4):
                if i == 3:
                    print("회원이 아닙니다.")
                    breaker = True
                    break
                pw = input("비밀번호: ")
                if pw == 'xxx123':
                    total = int(total*0.9)
                    print("10% 할인됩니다. 결제 가격: ", total)
                    breaker = True
                    break
                else:
                    print("비밀번호가 틀렸습니다.")
            if breaker:
                break
        else:
            print("회원이 아닙니다.")
            break # 들여쓰기 2번 된 와일이 있는지 찾음 -> 없으면 1번된 와일 -> 벽에 분은 와일
    elif m == 'n':
        break
    else:
        print("다시입력해주세요")

while True:
    print("담긴 상품: ", basket)
    print("결제할 금액: ", total)
    y = int(input("결제해주세요. 금액 투입: "))

    if y >= total:
        print("결제가 완료되었습니다.", "잔돈:", y - total)
        break
    else:
        print("금액이 부족합니다.")

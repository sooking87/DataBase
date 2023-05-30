import pymysql
import pandas as pd
from tabulate import tabulate


def show_product_list():
    # 구매 가능한 상품 보여주기
    print('구매 가능 내역입니다.')
    print('---------------------------------')
    # cursor를 이용해서 sql문 실행
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    # TOP 내역 출력하기
    print('TOP')
    top = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'TOP' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(top)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)

    print(tabulate(products, headers='keys',
          tablefmt='psql', showindex=True), '\n')

    # BOTTOM 내역 출력하기
    print('BOTTOM')
    bottom = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'BOTTOM' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(bottom)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)
    print(tabulate(products,
          tablefmt='psql', showindex=True), '\n')

    # SHOES 내역 출력하기
    print('SHOES')
    shoes = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'SHOES' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(shoes)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)

    print(tabulate(products,
          tablefmt='psql', showindex=True), '\n')

    # ACC 내역 출력하기
    print('ACC')
    acc = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'ACC' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(acc)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)
    print(tabulate(products,
          tablefmt='psql', showindex=True), '\n')

    cur.close()


def order():
    # 주문 처리 함수
    print('로그인창으로 넘어갑니다.')
    cusID = sign_in()
    if cusID == -1:
        return
    show_product_list()
    # cursor를 이용해서 sql문 실행
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    sql = 'SELECT DISTINCT PINFO FROM product'
    cur.execute(sql)

    rows = cur.fetchall()
    categories = [rows[i][0] for i in range(len(rows))]

    while True:
        print('카테고리: ', end=' ')
        print(categories)
        cate, num = input('어떤 상품을 구매하시겠습니까?(카테고리 제품번호): ').split()
        if cate in categories:
            # ROW_NUMBER를 이용해서 사용자가 원하는 카테고리의 번호만 입력으로도 주문 가능 상품인지 아닌지 조회하는 쿼리
            sql = 'SELECT * FROM(SELECT ROW_NUMBER() OVER(ORDER BY PRICE) AS num, PNO, PNAME, PRICE FROM product WHERE PINFO = "' + \
                cate + '") temp WHERE temp.num = ' + num
            cur.execute(sql)

            rows = cur.fetchall()
            if (rows):
                product = pd.DataFrame(rows)
                print(tabulate(product,
                               tablefmt='psql', showindex=False))
                print('상품 주문이 완료되었습니다.')
                # 해당 id의 사용자의 purchase에는 추가
                # product의 CNT는 -1
                # 카트에 있으면 지우기 없으면 걍 넘어가
                break
            else:
                print('해당 상품은 존재하지 않습니다. 다시 입력해주세요.')
        else:
            print('입력한 카테고리가 존재하지 않습니다. 다시 입력해주세요.')


def cart():
    # 카트에 상품 넣기
    print('cart()')


def customer_info():
    # 상품 내역 조회
    print('customer_info()')


def sign_up():
    # 회원 가입
    print('sign_up()')
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()

    newID = input('[필수] 사용할 ID를 입력해주세요: ')
    newNAME = input('[필수] 사용자의 이름을 입력해주세요: ')
    newAGE = int(input('[필수] 사용자의 나이를 입력해주세요: '))
    newSEX = int(input('[필수] 성별을 입력해주세요. (남(0) / 여(1)): '))
    newCITY = input('[필수] 주소지를 입력해주세요: ')
    newPhoneNUM = input('[선택] 사용자의 전화번호를 입력해주세요: ')

    SEX = ''
    if newSEX == 0:
        SEX = 'MALE'
    elif newSEX == 1:
        SEX = 'FEMALE'

    sql = 'insert into `Product-Purchase-History-Management` `customer` values (%s %s %d %s %s %s)'
    val = (newID, newNAME, newAGE, newPhoneNUM, newCITY, SEX)
    cur.execute(sql, val)
    rows = cur.fetchall()

    print('\n가입이 완료되었습니다.\n')


def sign_in():
    # 로그인 하기
    # DB 연결
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    sql = 'SELECT CusID FROM customer'
    cur.execute(sql)

    rows = cur.fetchall()
    ids = [rows[i][0] for i in range(len(rows))]
    cusID = ''

    while True:
        cusID = input('사용자 ID를 입력해주세요: ')
        if cusID in ids:
            print('로그인 되었습니다.')
            return cusID
        else:
            print('사용자의 ID가 회원 가입이 되지 않았습니다. 회원 가입 후 이용해주시기 바랍니다.')
            return -1


def resign():
    # 회원 탈퇴
    print('resign()')


def start():
    print('-------------------------')
    print('메뉴를 선택해주세요.')
    print('1. 회원 가입하기')
    print('2. 회원 탈퇴하기')
    print('3. 구매 가능한 상품 내역 보기')
    print('4. 상품 주문하기')
    print('5. 카트 확인하기')
    print('0. 종료')
    print('\n')

    menu = input('메뉴 번호를 입력해주세요.: ')

    return menu


# show_product_list()

while True:
    menu = start()

    if menu == '1':
        sign_up()
    elif menu == '2':
        resign()
    elif menu == '3':
        show_product_list()
    elif menu == '4':
        order()
    elif menu == '5':
        cart()
    elif menu == '0':
        print('서비스를 이용해주셔서 감사합니다.')
        break

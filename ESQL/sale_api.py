import pymysql
import pandas as pd
from tabulate import tabulate
import re
from random import randint
import datetime

def show_product_list():
    # 구매 가능한 상품 보여주기
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
    headers = ['상품명', '가격']
    print(tabulate(products, headers=headers, 
          tablefmt='psql', showindex=True), '\n')

    # BOTTOM 내역 출력하기
    print('BOTTOM')
    bottom = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'BOTTOM' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(bottom)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)
    print(tabulate(products, headers=headers,
          tablefmt='psql', showindex=True), '\n')

    # SHOES 내역 출력하기
    print('SHOES')
    shoes = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'SHOES' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(shoes)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)

    print(tabulate(products, headers=headers,
          tablefmt='psql', showindex=True), '\n')

    # ACC 내역 출력하기
    print('ACC')
    acc = "SELECT PNAME, PRICE FROM product WHERE `PINFO` = 'ACC' AND `CNT` >= 0 AND `CNT` <= 10000 ORDER BY `PRICE`"
    cur.execute(acc)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)
    print(tabulate(products, headers=headers,
          tablefmt='psql', showindex=True), '\n')

    cur.close()

def order():
    # 주문 처리 함수
    print('로그인창으로 넘어갑니다.')
    cusID, cusPW = sign_in()
    if cusID == -1 and cusPW == -1:
        return
    show_product_list()
    # cursor를 이용해서 sql문 실행
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8', autocommit=True)
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
            sql = 'SELECT * FROM(SELECT ROW_NUMBER() OVER(ORDER BY PRICE) AS num, PNO, PNAME, PRICE, CNT FROM product WHERE PINFO=%s) temp WHERE temp.num=%s'
            val = (cate, num)
            cur.execute(sql, val)

            rows = cur.fetchall()
            cnt = rows[0][4]
            # CNT가 1이상이므로(테이블 제약조건에 있음) 주문이 가능하다면
            if (rows):
                # product = pd.DataFrame(rows)
                # print(tabulate(product,
                #                tablefmt='psql', showindex=False))
                ordered_pno = rows[0][1]
                # print('상품 주문이 완료되었습니다.')

                # 주문한 상품(product TABLE)을 상품내역 리스트(purchase TABLE)에 추가하기
                # 카트(cart TABLE)에 해당 물품이 있다면 주문했으므로 삭제하기

                # 주문한 상품 아이디와 고객 아이디를 바탕으로 카트에 존재를 하는지
                sql2 = 'SELECT * FROM cart, customer, product WHERE customer.CusID = cart.CusID AND product.PNO = cart.PNO AND product.PNO=%s AND customer.CusID=%s'
                val = (ordered_pno, cusID)
                cur.execute(sql2, val)
                
                is_in_cart = cur.fetchall()
                indate = None
                if is_in_cart:
                    indate = is_in_cart[0][2]
                
                    
                # product TABLE에서 수량(CNT) -1하기
                # print(indate)
                cnt -= 1
                update = 'UPDATE product SET CNT=%s WHERE PNO=%s'
                val = (cnt, ordered_pno)
                cur.execute(update, val)
                # print('product CNT 업데이트 완료')
                
                # 주문하려는 상품이 카트에 존재하지 않다면 그냥 사용자 정보만 보여주면 됨.
                # purchase TABLE에는 INSERT
                # 배달 기사의 경우 랜덤으로 배정
                delivery_person = randint(1, 10)
                assign_dp = 'SELECT DNO FROM(SELECT ROW_NUMBER() OVER(ORDER BY DNO) AS num, DNO FROM deliveryperson) temp WHERE temp.num=%s'
                cur.execute(assign_dp, delivery_person)

                rows = cur.fetchall()
                # print(rows[0][0], '택배 기사 배정 완료')
                charge = rows[0][0]
                # DATE 칼럼의 경우는 현재 INSERT 하는 시간 기준
                now = datetime.datetime.now()
                date = str(now.strftime('%Y-%m-%d-%H:%M'))

                insert = 'INSERT INTO `Product-Purchase-History-Management`.`purchase` (`PNO`, `CusID`, `DNO`, `DATE`) VALUES(%s, %s, %s, %s)'
                val = (ordered_pno, cusID, charge, date)
                cur.execute(insert, val)
                # print('purchase TABLE update 완료')

                if is_in_cart:
                    # 주문 완료 후 성함, 의류 카테코리, 가격, 상품명, 주문 시간, 배당된 택배기사 번호, 카트에 넣은 날짜를 출력하기 위한 쿼리문
                    notice = 'SELECT customer.CusNAME, product.PINFO, product.PRICE, product.PNAME, purchase.DATE, deliveryperson.DNAME, cart.InDATE FROM customer, product, purchase, deliveryperson, cart WHERE customer.CusID=purchase.CusID AND purchase.PNO=product.PNO AND purchase.DNO=deliveryperson.DNO AND cart.CusID=customer.CusID AND customer.CusID=%s AND product.PNO=%s AND deliveryperson.DNO=%s AND cart.InDATE=%s'
                    val = (cusID, ordered_pno, charge, indate)
                    cur.execute(notice, val)
                else:
                    # 주문 완료 후 성함, 의류 카테코리, 가격, 상품명, 주문 시간, 배당된 택배기사 번호 넣은 날짜를 출력하기 위한 쿼리문
                    notice = 'SELECT customer.CusNAME, product.PINFO, product.PRICE, product.PNAME, purchase.DATE, deliveryperson.DNAME FROM customer, product, purchase, deliveryperson WHERE customer.CusID=purchase.CusID AND purchase.PNO=product.PNO AND purchase.DNO=deliveryperson.DNO AND customer.CusID=%s AND product.PNO=%s AND deliveryperson.DNO=%s'
                    val = (cusID, ordered_pno, charge)
                    cur.execute(notice, val)

                rows = cur.fetchall()
                result = pd.DataFrame(rows)
                print('\n%s님 상품 주문이 완료되었습니다.\n' %cusID)
                print(tabulate(result, 
                        tablefmt='psql', showindex=False))
                # print(is_in_cart)
                # 주문하려는 상품이 카트에 존재한다면
                if is_in_cart:
                    # cart TABLE에 있는 상품은 DELETE
                    # print("조회한 결과: ")
                    # print(tabulate(product,
                    #             tablefmt='psql', showindex=False))
                    sql = 'DELETE FROM cart WHERE cart.PNO=%s AND cart.CusID=%s'
                    val = (ordered_pno, cusID)
                    cur.execute(sql, val)
                print('감사합니다.')
                break
            else:
                print('해당 상품은 존재하지 않습니다. 다시 입력해주세요.')
        else:
            print('입력한 카테고리가 존재하지 않습니다. 다시 입력해주세요.')
    cur.close()

def cart():
    # 카트에 상품 넣기
    print('로그인창으로 넘어갑니다.')
    cusID, cusPW = sign_in()
    if cusID == -1 and cusPW == -1:
        return
    show_product_list()
    # cursor를 이용해서 sql문 실행
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8', autocommit=True)
    cur = db.cursor()
    sql = 'SELECT DISTINCT PINFO FROM product'
    cur.execute(sql)

    rows = cur.fetchall()
    categories = [rows[i][0] for i in range(len(rows))]

    while True:
        print('카테고리: ', end=' ')
        print(categories)
        cate, num = input('어떤 상품을 카트에 넣겠습니까?(카테고리 제품번호): ').split()

        if cate in categories:
            # ROW_NUMBER를 이용해서 사용자가 원하는 카테고리의 번호만 입력으로도 주문 가능 상품인지 아닌지 조회하는 쿼리
            sql = 'SELECT * FROM(SELECT RANK() OVER(ORDER BY PRICE) AS num, PNO, PNAME, PRICE, CNT FROM product WHERE PINFO=%s) temp WHERE temp.num=%s'
            val = (cate, num)
            cur.execute(sql, val)

            rows = cur.fetchall()
            # CNT가 1이상이므로 카트에 넣기
            if (rows):
                cart_pno = rows[0][1]
                
                # DATE 칼럼의 경우는 현재 INSERT 하는 시간 기준
                now = datetime.datetime.now()
                date = str(now.strftime('%Y-%m-%d-%H:%M'))

                insert = 'INSERT INTO `Product-Purchase-History-Management`.`cart` (`CusID`, `PNO`, `InDATE`) VALUES(%s, %s, %s)'
                val = (cusID, cart_pno, date)
                cur.execute(insert, val)

                print('\n%s님 상품을 카트에 담았습니다.\n' %cusID)
                break
            else:
                print('해당 상품은 존재하지 않습니다. 다시 입력해주세요.')
        else:
            print('입력한 카테고리가 존재하지 않습니다. 다시 입력해주세요.')
    cur.close()


def customer_info():
    # 상품 내역 조회
    print('\n로그인창으로 넘어갑니다.\n')
    cusID, cusPW = sign_in()
    if cusID == -1 and cusPW == -1:
        return
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    sql = "SELECT PINFO, PNAME, PRICE, DATE FROM product, customer, purchase WHERE customer.CusID = purchase.CusID AND product.PNO = purchase.PNO AND customer.CusID=%s AND CusPW=%s"
    val = (cusID, cusPW)
    cur.execute(sql, val)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)

    print("%s님의 주문 내역 조회 결과입니다." %cusID)
    print(tabulate(products, headers=('카테고리', '상품명', '가격', '주문 날짜'),
          tablefmt='psql', showindex=False), '\n')
    cur.close()

def check_cart():
    # 카트 내역 조회
    print('\n로그인창으로 넘어갑니다.\n')
    cusID, cusPW = sign_in()
    if cusID == -1 and cusPW == -1:
        return
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    sql = "SELECT PINFO, PNAME, PRICE, InDATE FROM product, customer, cart WHERE customer.CusID = cart.CusID AND product.PNO = cart.PNO AND customer.CusID=%s AND customer.CusPW=%s"
    val = (cusID, cusPW)
    cur.execute(sql, val)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)

    print("%s님의 카트 내역 조회 결과입니다." %cusID)
    print(tabulate(products, headers=('카테고리', '상품명', '가격', '넣은 날짜'),
          tablefmt='psql', showindex=False), '\n')
    cur.close()

def format_phone_number(input):
    # xxx-xxxx-xxxx 형식으로 전화번호를 세팅해주는 함수
    phone_num = re.sub(r'[^0-9]', '', input)
    result = ""
    length = len(phone_num)
    
    if length == 8:
        result = re.sub(r'(\d{4})(\d{4})', r'\1-\2', phone_num)
    elif phone_num.startswith("02") and (length == 9 or length == 10):
        result = re.sub(r'(\d{2})(\d{3,4})(\d{4})', r'\1-\2-\3', phone_num)
    elif not phone_num.startswith("02") and (length == 10 or length == 11):
        result = re.sub(r'(\d{3})(\d{3,4})(\d{4})', r'\1-\2-\3', phone_num)
    else:
        result = None

    return result

def sign_up():
    # 회원 가입
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8', autocommit=True)
    cur = db.cursor()

    newID = input('[필수] 사용할 ID를 입력해주세요: ')
    newPW = input('[필수] 사용자의 Password를 입력해주세요: ')
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
    
    phone_num = ''
    if newPhoneNUM != '':
        phone_num = format_phone_number(newPhoneNUM)
    else:
        phone_num = None

    sql = 'SELECT * FROM `customer` WHERE CusID=%s AND CusPW=%s'
    val = (newID, newPW)
    cur.execute(sql, val)
    rows = cur.fetchall()

    if (rows):
        print('\n이미 존재하는 ID입니다.\n')
    else:
        sql = 'INSERT INTO `Product-Purchase-History-Management`.`customer` (`CusID`, `CusPW`, `CusNAME`, `AGE`, `PhoneNUM`, `CITY`, `SEX`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        # INSERT INTO `Product-Purchase-History-Management`.`customer` (`CusID`, `CusNAME`, `AGE`, `PhoneNUM`, `CITY`, `SEX`) VALUES('s', 'sd', 23, '010-1111-1113', '분당구', 'FEMALE')
        val = (newID, newPW, newNAME, newAGE, phone_num, newCITY, SEX)
        cur.execute(sql, val)
        rows = cur.fetchall()

        print('\n가입이 완료되었습니다.\n')
    cur.close()

def sign_in():
    # 로그인 하기
    # DB 연결
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    
    cusID = ''
    cusPW = ''
    cusID = input('사용자 ID를 입력해주세요: ')
    
    sql = 'SELECT * FROM customer WHERE CusID=%s'
    cur.execute(sql, cusID)

    pass_ID = cur.fetchall()
    if pass_ID:
        while True:
            cusPW = input('사용자 PW를 입력해주세요: ')
            sql = 'SELECT * FROM customer WHERE CusID=%s AND CusPW=%s'
            personal = (cusID, cusPW)
            cur.execute(sql, personal)
            pass_PW = cur.fetchall()
            if pass_PW:
                print('\n로그인 되었습니다.\n')
                break
            else:
                print('\n비밀번호가 틀렸습니다. 다시 입력해주세요.\n')
        return cusID, cusPW
    else:
        print('\n사용자의 ID가 회원 가입이 되지 않았습니다. 회원 가입 후 이용해주시기 바랍니다.')
        return -1, -1
    

def check_pw():
    # 비밀번호 조회하기
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()

    id = input('비밀번호를 조회할 [아이디]를 입력해주세요: ')
    sql = 'SELECT CusPW FROM customer WHERE CusID=%s'
    cur.execute(sql, id)

    rows = cur.fetchall()

    if rows:
        print('\n%s님의 아이디는 %s입니다.\n' %(id, rows[0][0]))
    else:
        print('\n존재하지 않는 아이디입니다. 회원 가입해주세요\n')
    cur.close()



def resign():
    # 회원 탈퇴
    print('로그인창으로 넘어갑니다.')
    cusID, cusPW = sign_in()
    if cusID == -1 and cusPW == -1:
        return
    
    # cursor를 이용해서 sql문 실행
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8', autocommit=True)
    cur = db.cursor()
    yes = ['y', 'Y', 'yes', 'Yes', 'YES']
    no = ['n', 'N', 'no', 'No', 'NO']
    while True:
        ans = input('정말 회원 탈퇴를 하시겠습니까?(y/n): ')
        if ans in yes:
            sql = 'DELETE FROM customer WHERE CusID=%s AND CusPW=%s'
            val = (cusID, cusPW)
            cur.execute(sql, val)

            print('\n회원 탈퇴가 완료되었습니다.\n')
        elif ans in no:
            print('\n회원 탈퇴를 취소합니다.\n')
        break
    cur.close()        
        
def check_cnt():
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()

    cnt = "SELECT PNAME, CNT FROM product"
    cur.execute(cnt)
    rows = cur.fetchall()
    products = pd.DataFrame(rows)
    headers = ['상품명', '수량']
    print(tabulate(products, headers=headers, 
          tablefmt='psql', showindex=False), '\n')

def start():
    print('-------------------------')
    print('메뉴를 선택해주세요.')
    print('1. 회원 가입하기')
    print('2. 회원 탈퇴하기')
    print('3. 비밀번호 조회하기')
    print('4. 구매 가능한 상품 내역 보기')
    print('5. 상품 주문하기')
    print('6. 카트에 상품 넣기')
    print('7. 주문 내역 조회하기')
    print('8. 카트 내역 조회하기')
    print('9. 상품 수량 확인하기')
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
        check_pw()
    elif menu == '4':
        show_product_list()
    elif menu == '5':
        order()
    elif menu == '6':
        cart()
    elif menu == '7':
        customer_info()
    elif menu == '8':
        check_cart()
    elif menu == '9':
        check_cnt()
    elif menu == '0':
        print('\n서비스를 이용해주셔서 감사합니다.\n')
        break

import pymysql
import pandas as pd
from tabulate import tabulate


# 사용자가 있는 사람인지 아닌지 확인하기
def order():
    # 주문 처리 함수
    # DB 연결
    db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
                         charset='utf8')
    cur = db.cursor()
    sql = 'SELECT CusID FROM customer'
    cur.execute(sql)

    rows = cur.fetchall()
    ids = [rows[i][0] for i in range(len(rows))]

    while True:
        cusID = input('사용자 ID를 입력해주세요: ')
        if cusID in ids:
            print('로그인 되었습니다.')
        else:
            print('사용자의 ID가 회원 가입이 되지 않았습니다. 회원 가입 후 이용해주시기 바랍니다.')

    # cate, num = input('어떤 상품을 구매하시겠습니까?(카테고리 제품번호): ')
order()

import pymysql
import pandas as pd
from tabulate import tabulate
from random import randint
import datetime

# db = pymysql.connect(host='localhost', user='root', password='sks0hn01!!', db='product-purchase-history-management',
#                          charset='utf8')
# cur = db.cursor()
# top = "SELECT * FROM deliveryperson"
# cur.execute(top)
# rows = cur.fetchall()
# products = pd.DataFrame(rows)

# print(tabulate(products, headers='keys',
#         tablefmt='psql', showindex=True), '\n')
# print(len(products))
# print(randint(1, len(products)))
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d-%H:%M')
print(date)
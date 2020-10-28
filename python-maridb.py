# python-maridb.py

import pymysql
import jieba

f = open('c:/tmp/hamlet.txt','rt')
word = f.read().split(' ')
f.close()

db_connect = pymysql.connect('192.168.1.235', 'root', '   ','test')
cursor = db_connect.cursor()
for w in word:
    sql = 'insert into t (word) value ("{}")'.format(w)
    cursor.execute(sql)
    db_connect.commit()
db_connect.close()
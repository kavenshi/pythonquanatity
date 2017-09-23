#codeing=utf-8
from dytt8.dytt8 import dytt8
import sqlite3

db= sqlite3.connect('./spider.db')
link = db.cursor()
link.execute('slect * from sqlite_master where type ="table" and name="ftp_url";')
if not link.fetchone():
    link.execute("""CREAT TABLE 'ftp_url'('id' INTEGER PRIMARY KEY NOT NULL,'url' varchar(120) DEFAULT NULL)""")
    db.commit()
print("开始爬取")
dytt = dytt8(5)
# for url in urls:
#     sql="""INSERT INTO 'ftp_url' value(NULL,'%s');"""%(url)
#     link.execute(sql)
db.commit()
db.close()

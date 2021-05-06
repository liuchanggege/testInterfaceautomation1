'封装连接数据的方法 用于 调用'
_author_ = 'liuchang'

import pymysql
class Mysql():

    def __init__(self):
        self.conn=pymysql.connect(host = '10.211.55.3',user = 'root',password = '123456',port = 3306,db = 'bugfree',charset = 'utf8')#建立连接
        self.couser = self.conn.cursor(pymysql.cursors.DictCursor)  # 建立游标，返回结果是字典。如果不加参数，返回元组

    def returnall(self):

        sql1='select * from bf_user_log' #要执行的sql
        self.couser.execute(sql1) #执行sql
        data=self.couser.fetchall() # 返回所有行
        self.couser.close()
        self.conn.close()
        return data

    def returnone(self):
        sql = 'select * from bf_user_log'  # 要执行的sql
        self.couser.execute(sql)  # 执行sql
        data = self.couser.fetchone()  # 只返回一行
        self.couser.close()
        self.conn.close()
        return data

    def insertsql(self,sql="insert into bf_user_log (created_at,created_by,ip) values ('2019-11-18 17:20:00',1,'11.1.1.1')"):

        self.couser.execute(sql)
        self.conn.commit()
        self.couser.close()
        self.conn.close()

    def updatesql(self,sql="update bf_user_log set ip='2,2,22.2' where id=3"):

        self.couser.execute(sql)
        self.conn.commit()
        self.couser.close()
        self.conn.close()

    def deletesql(self,sql="delete from bf_user_log where id=3"):

        self.couser.execute(sql)
        self.conn.commit()
        self.couser.close()
        self.conn.close()

if __name__ == '__main__':
    a=Mysql()
    print(a.deletesql())

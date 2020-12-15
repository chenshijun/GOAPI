import pymysql
from util.Logger import Logger

log = Logger().get_log()


class MysqlHelper(object):

    def __init__(self, host, username, password, db, charset="utf8", port=3306):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=username, password=password, db=db, charset=charset)
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            log.error("数据库连接失败:{a}".format(a=str(e)))
            raise Exception("数据库连接失败")

    def util(fun):
        def wrapper(self, sql):
            try:
                self.execute(sql=sql)
                d = fun(self, sql)
                self.close()
                return d
            except Exception as e:
                log.error("执行数据库操作失败:{a}".format(a=str(e)))

        return wrapper

    def execute(self, sql):
        self.cursor.execute(sql)

    def close(self):
        self.cursor.close()
        self.conn.close()

    @util
    def fetchone(self, sql):
        return self.cursor.fetchone()

    @util
    def fetchall(self, sql):
        return self.cursor.fetchall()

    def execute(self, sql):
        self.cursor.commit()
        num = self.cursor.rowcount
        return num

    @property
    def rowcount(self):
        return self.cursor.rowcount

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

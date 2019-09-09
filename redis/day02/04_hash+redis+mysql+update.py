"""
hash + redis + mysql + update
更新数据，更新redis
"""
import redis
import pymysql


class Update():
    def __init__(self):
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            database='mysite',
        )
        self.r = redis.Redis()
        self.cursor = self.db.cursor()

    # 更新MySQL记录
    def update_mysql(self, new_age, userID):

        sql = 'update user_author set age={} where id={}'.format(new_age, userID)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print('服务器正忙，请稍后再试', e)

    # 同步更新redis
    def update_redis(self, new_age, userID):
        result = self.r.hgetall(userID)
        if result:
            # 存在，更新特定字段的值
            self.r.hset(userID, 'age', new_age)
        else:
            # 不存在，缓存整个用户信息
            self.select_mysql(userID)


    def select_mysql(self, userID):
        sql = 'select * from user_author where id={}'.format(userID)
        self.cursor.execute(sql)
        userinfo = self.cursor.fetchall()
        # 得到最新数据缓存到redis中
        user_dict = {
            'id': userinfo[0][0],
            'username': userinfo[0][1],
            'age': userinfo[0][2],
            'email': userinfo[0][3],
        }
        self.r.hmset(userID, user_dict)
        # 设置过期时间
        self.r.expire(userID, 60)

    def main(self):
        userID = int(input('请输入用户ID:'))
        new_age = int(input('请输入新年龄:'))
        if self.update_mysql(new_age, userID):
            self.update_redis(new_age, userID)
        else:
            print('服务器正忙，请稍后再试')


if __name__ == '__main__':
    # 对象.属性
    syn = Update()
    syn.main()

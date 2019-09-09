"""
hash + redis + mysql
联合查询数据
"""
import redis
import pymysql

# 连接redis
r = redis.Redis()
# 连接mysql
p = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='mysite',
)

# mysql创建游标
cursor = p.cursor()

# 1.输入要查询的用户名
# 2.先到redis查询
# 3.redis如果没有查找到，再到MySQL查询


# hash: key field value
#       ID  字段名  对应值
#        1  name   王老师
#            age     28

userID = int(input('请输入用户ID:'))
result = r.hgetall(userID)


# 如果存在数据
if result:
    print('redis:', result)
else:
    # 1.到MySQL查询数据， 返回给用户
    # 2.缓存到redis中，并设置一个缓存时间
    sql = 'select * from user_author where id = {};'.format(userID)
    cursor.execute(sql)
    userinfo = cursor.fetchall()
    if not userinfo:
        print('用户不存在')
    else:
        print('mysql:', userinfo)
        # 缓存到redis
        user_dict = {
            'id': userinfo[0][0],
            'username': userinfo[0][1],
            'age': userinfo[0][2],
            'email': userinfo[0][3],
        }
        r.hmset(userID, user_dict)
        # 设置过期时间
        r.expire(userID, 60)


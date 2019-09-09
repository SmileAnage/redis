"""
Python操作字符串
"""
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


# 1.字符串操作
r.set('user001:name', 'xiaomu')
m_dict = {
    'user001:age': 23,
    'user001:gender': 'M',
}
r.mset(m_dict)

print(type(r.get('user001:name')))
print(type(r.mget('user001:name', 'user001:age')))
# 打印字符长度
print(r.strlen('user001:name'))

# 2.数值类操作
# 增加一
r.incr('user001:age')
print(r.get('user001:age'))
# 减去一
r.decr('user001:age')
print(r.get('user001:age'))

# 增加多数
r.incrby('user001:age', 10)
print(r.get('user001:age'))

# 同时减去多数
r.decrby('user001:age', 10)
print(r.get('user001:age'))

# 增加浮点数(可为负数)
r.incrbyfloat('user001:age', 1.5)
print(r.get('user001:age'))
r.incrbyfloat('user001:age', -1.5)
print(r.get('user001:age'))
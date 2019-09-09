"""
操作列表
"""
import redis

r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    db=1,
    password=None
)

r.rpush('tedu:teachers', 'laoQi', 'Matia', 'LaoGuo')
r.rpush('tedu:teachers', 'xiaoChaoChao')

# 在Maria的后面增加LaoTao
r.linsert('tedu:teachers', 'after', 'Matia', 'LaoTao')
# 设置过期时间
r.expire('tedu:teachers', 20)

# 打印长度
print(r.llen('tedu:teachers'))

# 查看所有元素
print(r.lrange('tedu:teachers', 0, -1))
# for i in r.lrange('tedu:teachers', 0, -1):
#     print(i.decode())

# 弹出一个元素
r.rpop('tedu:teachers')
print(r.lrange('tedu:teachers', 0, -1))

# 保留指定范围内的元素
r.ltrim('tedu:teachers', 0, 2)
print(r.lrange('tedu:teachers', 0, -1))

# 阻塞弹出
while True:
    r.brpop('tedu:teachers', 3)
    print(r.lrange('tedu:teachers', 0, -1))
    if not r.lrange('tedu:teachers', 0, -1):
        break

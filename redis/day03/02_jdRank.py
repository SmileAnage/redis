"""
京东手机畅销榜
"""
import redis

r = redis.Redis()

# 创建有序集合
day01_dict = {
    'huawei': 5000,
    'oppo': 4000,
    'iphone': 3000,
}

day02_dict = {
    'huawei': 5200,
    'oppo': 4200,
    'iphone': 3200,
}

day03_dict = {
    'huawei': 5300,
    'oppo': 4300,
    'iphone': 3300,
}

r.zadd('mobile:001', day01_dict)
r.zadd('mobile:002', day02_dict)
r.zadd('mobile:003', day03_dict)

# 求并集，mobile:001-003
r.zunionstore(
    'mobile:001-003',
    ('mobile:001', 'mobile:002', 'mobile:003'),
    aggregate='max',
)

# 求排名：zrevrange withscores是否显示value
result = r.zrevrange('mobile:001-003', 0, 2, withscores=True)

# 打印输出
num = 0
for i in result:
    num += 1
    print('第{}名: {}, 销量为：{}'.format(num, i[0].decode(), int(i[1])))

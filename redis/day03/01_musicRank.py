"""
音乐排行榜，利用有序集合

需求：
    排行榜前三名，以及播放量
"""
import redis

r = redis.Redis()

# 有序集合  -  sing:rank
r.zadd('song:rank',{
    '体面': 0,
    '山楂树恋人': 0,
    '往后余生': 0,
    '暗恋是一个人的事': 0,
})

# 增加峰值
r.zincrby('song:rank', 100, '体面')
r.zincrby('song:rank', 90, '山楂树恋人')
r.zincrby('song:rank', 80, '往后余生')
r.zincrby('song:rank', 70, '暗恋是一个人的事')

# 查看排名
result = r.zrevrange('song:rank', 0, 2, True)

# 得到的是个列表中的元组
num = 0
for i in result:
    num += 1
    print("第{}名：{}, 播放量：{}".format(num, i[0].decode(), int(i[1])))

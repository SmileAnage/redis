"""
常见端口号

mysql   3306
Mongodb 27017
redis   6379
http    80
https   443
ssh     22
telnet  23
ftp     21

"""
import redis

# 创建连接对象
# 数据库db 只有0-15
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    db=1,
    password=None
)

# 通用命令示例
# 显示所有信息
key_list = r.keys('*')
print(key_list)

# 循环显示
for i in key_list:
    print(i.decode())

# 返回字符格式
print(r.type('mylist2').decode())

# 查看是否在数据库中, return 0 | 1
print(r.exists('mylist2'))

# 设置过期时间
r.expire('mylist2', 5)

# 删除key
r.delete('mylist2')


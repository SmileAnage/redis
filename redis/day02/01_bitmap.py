"""
位图操作寻找活跃用户
"""
import redis

r = redis.Redis()


# user = ['user:001','user:002','user:003','user:004',]

# user:001 一年中第5天和第200天登录
r.setbit('user:001', 4, 1)
r.setbit('user:001', 199, 1)

# user:002 一年中第100天和第300天登录
r.setbit('user:002', 99, 1)
r.setbit('user:002', 299, 1)

# user:003 一年中登录了100次以上
for i in range(0, 366, 2):
    r.setbit('user:003', i, 1)
print(r.bitcount('user:003', 0, 366))

# user:004 一年中登录了100次以上
for i in range(0, 366, 3):
    r.setbit('user:004', i, 1)

# 列表接收数据
user_list = r.keys('user:*')


# 存放活跃用户
active_users = []

# 存放不活跃用户
noactive_users = []

# 遍历数据
for user in user_list:
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_users.append((user, login_count))
    else:
        noactive_users.append((user, login_count))

print('活跃用户:', active_users)
print('不活跃用户:', noactive_users)
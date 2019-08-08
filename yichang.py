# -*- utf:8 -*-
# 捕获异常
try:
    11/0
except Exception as ret:
    print('异常提醒消息')
    print(ret)  # as 变量 获取异常名字
else:
    print('无异常')
finally:
    print('不管有没有异常都会执行finally')

    # raise 抛出异常

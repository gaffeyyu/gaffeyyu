import time

activity = 0

while True:
    # 模拟用户的一些活动
    time.sleep(5)
    activity += 1

    # 每隔一段时间打印出当前的活跃度
    if activity % 5 == 0:
        print("当前活跃度：", activity)

import time

def pomodoro_timer():
    print("开始专注时间！")
    for i in reversed(range(1, 26)):
        minutes = i // 60
        seconds = i % 60
        print(f"还有 {minutes:02d}:{seconds:02d}...")
        time.sleep(1)
    print("休息时间到了！")

while True:
    pomodoro_timer()
    print("休息一下，开始下一个番茄时间。")
    time.sleep(300)  # 休眠5分钟，以便专注一段时间后再次集中注意力

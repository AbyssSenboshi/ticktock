import time

def focus_timer(minutes):
    seconds = minutes * 60
    while True:
        if seconds == 0:
            print("Time's up!")
            break
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

focus_timer(25)  # 设置专注时长为25分钟

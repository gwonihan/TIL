import time

# Epoch time
# print(time.time()) #현재 시간을 실수형으로 보여줌

# 시간 변환
# print(time.localtime(time.time()))
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=19, tm_hour=10, tm_min=49, tm_sec=31, tm_wday=2, tm_yday=19, tm_isdst=0)

# 시간 변환
# print(time.asctime(time.localtime(time.time())))
# Wed Jan 19 10:51:26 2022

# print(time.ctime())
# Wed Jan 19 10:52:17 2022

# 시간 포맷 (우리와 시간을 표기하는 법이 달라서 사용)
# print(time.strftime('%x', time.localtime(time.time())))
# 01/19/22
                    #'%c': 알파벳을 다르게해서 옵션을 줄 수있다. https://strftime.org/
# print(time.strftime('%c', time.localtime(time.time())))
# Wed Jan 19 10:54:40 2022

# 많이 쓰게될 것임, time.sleep() 괄호안에 있는 간격으로 시간을 찍는다
for i in range(5):
    print(time.ctime())
    time.sleep(5)


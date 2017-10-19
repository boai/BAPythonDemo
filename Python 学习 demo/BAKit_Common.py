
import time, calendar


# 格式当前日期时间，例如：2017-10-19 14:24:41
def ba_getCurrentTimeWithYMDHMS():
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return currentTime

# currentTime = ba_getCurrentTimeWithYMDHMS()
# print(currentTime)

# 获取指定年月的日历
def ba_getCurrentCalendarWithMonth(year, month):
    currentCalendar = calendar.month(year, month)
    return currentCalendar

# currentCalendar = ba_getCurrentCalendarWithMonth(2017, 10)
# print(currentCalendar)


import datetime

dt_now = datetime.datetime.now()
year = str(dt_now.year)
month = str(dt_now.month)
day = str(dt_now.day)
hour = str(dt_now.hour)
min = str(dt_now.minute)
data_day = year + "," + month + day + "," + hour + min
print(data_day)

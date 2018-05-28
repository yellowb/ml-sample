from datetime import datetime, timedelta, timezone

"""Samples of using datetime built-in module"""

# now
now = datetime.now()
print(now)

# constructor
dt = datetime(2018, 5, 23, 20, 30, 0)
print(dt)

# timestamp
ts = dt.timestamp()
print(ts)

# timestamp -> datetime
dt = datetime.fromtimestamp(ts)
print(dt)
utc_dt = datetime.utcfromtimestamp(ts)
print(utc_dt)

# str -> datetime. Ref: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
dt = datetime.strptime('20180523203000.555', '%Y%m%d%H%M%S.%f')
print(dt)

# datetime -> str
dt_str = dt.strftime('%Y%m%d%H%M%S.%f')
print(dt_str)

# add or sub on datetime
dt = dt + timedelta(hours=1)
print(dt)
dt = dt + timedelta(minutes=-10)
print(dt)

# change timezone(default tzinfo of a datetime object is None)
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区
utc_dt = datetime.utcnow()
print(utc_dt)
utc_dt = utc_dt.replace(tzinfo=timezone.utc)  # you have to force set the tzinfo, but no change the time value
print(utc_dt)
beijing_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # force change timezone to +8, the display also changes
print(beijing_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))  # force change timezone to +9
print(tokyo_dt)


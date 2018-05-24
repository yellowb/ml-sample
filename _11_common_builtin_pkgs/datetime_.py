from datetime import datetime, timedelta

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

import pendulum

dt = pendulum.from_timestamp(-1)
print(dt)

dt2 = pendulum.from_timestamp(-1, tz='Europe/London')
print(dt2)

dt3 = pendulum.datetime(2008, 1, 1)
p = pendulum.instance(dt3)
print(p)

import pendulum

dt = pendulum.now()

# A period is the difference between 2 instances
period = dt - dt.subtract(days=3)

period.in_weeks()

# A period is iterable
for dt in period:
    print(dt)
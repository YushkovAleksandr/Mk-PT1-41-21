import timer

timer.start()
for i in range(10000000):
    i += 1
timer.finish()

timer.start()
for i in range(1000000):
    i += 1
timer.finish()

timer.start()
for i in range(100000000):
    i += 1
timer.finish()
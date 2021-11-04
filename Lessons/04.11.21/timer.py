import time

start_time = time.time()

def start():
    global start_time
    start_time = time.time()

def finish():
    print(f"{time.time()-start_time} seconds")
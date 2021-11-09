import datetime

def do_twice(func):
    def fgsdjklcghvjhdkhlh():
        print("starting")
        func()
        func()
        print("finishing")
    return fgsdjklcghvjhdkhlh

@do_twice
def hello():
    print("Hello, it's me")

# hello = do_twice(hello)

hello()

@do_twice
def show_current_time():
    print(datetime.datetime.now())

# show_current_time = do_twice(show_current_time)
show_current_time()
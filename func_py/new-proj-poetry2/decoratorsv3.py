from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

def my_decor(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decor
def say_whee():
    print("Whee!")

@not_during_the_night
def test_night():
    print("Time?")

# say_whee = not_during_the_night(say_whee)
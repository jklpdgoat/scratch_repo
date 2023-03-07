from decor import do_twice

@do_twice
def say_whee():
    print("Wheee! I am form another file.")

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
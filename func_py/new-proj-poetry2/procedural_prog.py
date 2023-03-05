def func1():
    pass

def func2():
    pass

def func3():
    pass

executing = lambda f: f()
#print(map(executing, [func1, func2, func3]))

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

starting_number = 96
print(starting_number)
square = starting_number ** 2
print(square)
increment = square + 1
print(increment)
cube = increment ** 3
print(cube)
decrement = cube - 1
print(decrement)
res = starting_number + cube
print(res)
from functools import reduce

# define a function `call` where you provide the function and the arguments
def call(x, f):
    return f(x)

# define a function that returns the square
square = lambda x : x * x

# define a function that returns the increment
increment = lambda x : x + 1

# define a function that returns the cube
cube = lambda x : x * x * x

# define a function that returns the decrement
decrement = lambda x : x - 1

funcs = [square, increment, cube, decrement]
# funcs = [square]
print(reduce(call, funcs, 96))
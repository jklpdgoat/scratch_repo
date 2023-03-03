list(map(int, ["1", "2", "3"]))

def hello_world(h):
    def world(w):
        print(h, w)
    return world # Returning functions

h = hello_world
x = h("hello")
print(x)
print(x("world"))

def naive_sum(list):
    s = 0
    for l in list:
        s += 1
    return s

print(naive_sum)
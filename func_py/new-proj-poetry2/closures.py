def add_5():
    five = 5

    # nesting functions
    def add(arg):
        return arg + five
    return add

if __name__ == '__main__':
    closure1 = add_5()
    print(closure1(1))
    print(closure1(2))
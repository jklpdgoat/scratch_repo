def check(f):
    # write your rode here or your wrapping function
    # return the wrapping function
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        if isinstance(res, dict):
            print("checked that the return value is dict.")
            return res
    return wrapper

@check
def my_code(args):
    # original functionality
    return {"lang": args}

print(my_code("python"))
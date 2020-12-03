def executor(*args, func=None):
    if not func:
        raise TypeError("Func is not passed")

    return map(func, *args)

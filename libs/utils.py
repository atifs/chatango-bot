import sys
import sys

def arguments(*args, **kwargs):
    args = ", ".join(repr(x) for x in args)
    kwargs = ", ".join(f"{x} = {y}" for x, y in kwargs.items())
    if args and kwargs:
        return "(" + ", ".join(args, kwargs) + ")"
    return "(" + (args or kwargs) + ")"

def event(func):
    def wraper(*args, **kwargs):
        print(f"{func.__name__}{arguments(*args, **kwargs)}", end=" -> ", file=sys.stderr)
        r = func(*args, *kwargs)
        print(r, file=sys.stderr)
        return r
    return wraper
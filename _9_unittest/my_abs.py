# a simple module used in demo unittest


# The same as `abs` function
def my_abs(x):
    if isinstance(x, (int, float)):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise TypeError()

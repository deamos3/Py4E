def factorial(x):
    # checks if x is an integer
    if not isinstance(x, int):
        return "please enter an integer"

    z = x
    # checks if x is zero, and returns 1
    if x == 0:
        return 1
    # checks if x is negative
    if x < 0:
        return "undefined: please restrict your input to non-negative integers"
    # iteratively performs factorial on x
    while x > 1:
        z = z * (x - 1)
        x -= 1
    return z
    # the response if x is not an integer

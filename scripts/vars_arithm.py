# Problem:
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.


def squareHypothenuse(a, b):
    return a * a + b * b


print(squareHypothenuse(817, 820))

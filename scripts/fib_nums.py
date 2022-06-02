# Problem
# Given: A positive integer n≤25.
# Return: The value of Fn.

# n beginning with 0 !
def get_fibonacci(n):
    before_before = 0
    before = 1

    i = 1  # because before before is 0 and before is 1 (i dont count one 0)
    fib = 0
    while i < n:
        fib = before_before + before
        # update before
        before_before = before
        before = fib
        i += 1

    print(fib)


get_fibonacci(21)

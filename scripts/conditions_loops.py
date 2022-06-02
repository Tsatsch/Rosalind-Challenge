# Problem
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.


def sum_of_odds(a, b):
    res = 0
    for i in range(a, b + 1):
        if i % 2 == 1:
            res += i
    return res


print(sum_of_odds(4430 , 9123))
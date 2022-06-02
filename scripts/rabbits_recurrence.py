# Problem
# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# rekursion
def rabbits(months, pairs):
    # trivial
    if months == 1:
        return 1
    elif months == 2:
        return pairs

    # calc recurrence relation Fn=Fn−1+Fn−2 (Fibonacci seq)
    first_gen = rabbits(months - 1, pairs)
    second_gen = rabbits(months - 2, pairs)

    # simple fibonacci for 3 and 4 months
    if months <= 4:
        return first_gen + second_gen

    return first_gen + (second_gen * pairs)


print(rabbits(35, 2))

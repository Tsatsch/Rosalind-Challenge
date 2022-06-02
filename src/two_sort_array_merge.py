# Problem
# Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105,
# a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.
# Return: A sorted array C[1..n+m] containing all the elements of A and B.

def get_all_arrs(filename):
    arrays = []
    with open(filename) as f:
        for line in f.readlines():
            arr = line.strip().split(" ")
            # convert to ints
            arr_int = []
            for num in arr:
                arr_int.append(int(num))

            arrays.append(arr_int)

    return arrays


# not algorithmic approach
def merge_sort(filename):
    arrays = get_all_arrs(filename)
    result = []
    for arr in arrays:
        for elem in arr:
            result.append(elem)
    return sorted(result)


file = "../resources/arrays.txt"
arr = merge_sort(file)
# print arr
for elem in arr:
    print(elem, end=" ")

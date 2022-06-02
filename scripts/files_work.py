# Problem
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.


def file_with_evenLines(filename):
    output = open("../resources/output.txt", "a")

    counter = 0
    with open(filename) as f:
        for line in f:
            counter += 1
            if counter % 2 == 0:
                output.write(line)
            else:
                pass


file = "../resources/file.txt"
file_with_evenLines(file)


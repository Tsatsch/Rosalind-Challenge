data_set = open("../resources/fasta2.txt")
dna_strings = []

# read file, save in dna_strings and print out
for line in data_set.readlines():
    if not line.startswith(">"):
        line = line.rstrip()
        dna_strings.append(list(line))  # saved each line in array  divided by chars

line_number = 0
for line in dna_strings:
    print(f'{line_number}:\t{line}')
    line_number += 1

# calculate the profile matrix

profile = [[
    0 for i in range(dna_strings.__len__())
]]


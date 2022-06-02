# Problem
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection.
# (If several possible consensus strings exist, then you may return any one of them.)


def read_fasta(fastaname):
    # convert multiple line seq to one line
    fasta = {}  # {header : seq}
    header = ""
    seq = ""
    firstline = True

    # save fasta multiline seq to single line
    with open(fastaname) as f:
        for line in f:
            if line.startswith(">"):
                if firstline:
                    header = line[1:]
                    firstline = False
                else:
                    fasta[header.strip()] = seq
                    seq = ""
                    header = line[1:]
            else:
                seq += line.strip()

        fasta[header.strip()] = seq
    return fasta


def make_profile(filename):
    seqs = list(read_fasta(filename).values())

    # split to chars
    splitted_seqs = []
    for seq in seqs:
        splitted_seqs.append(list(seq))

    # transpose splitted seqs
    splitted_seqs_t = list(map(list, zip(*splitted_seqs)))

    profile = [["A:"], ["C:"], ["G:"], ["T:"]]
    for arr in splitted_seqs_t:
        profile[0].append(str(arr.count("A")))
        profile[1].append(str(arr.count("C")))
        profile[2].append(str(arr.count("G")))
        profile[3].append(str(arr.count("T")))

    # transpose profile for consenus seq
    profile_t = list(map(list, zip(*profile)))
    profile_t.pop(0)  # remove ACGT column
    # convert to int
    profile_t_int = []
    for arr in profile_t:
        arr = list(map(int, arr))
        profile_t_int.append(arr)

    # calc consensus
    consensus = ""
    for arr in profile_t_int:
        max_occurance = max(arr)
        if arr.index(max_occurance) == 0:
            consensus += "A"
        elif arr.index(max_occurance) == 1:
            consensus += "C"
        elif arr.index(max_occurance) == 2:
            consensus += "G"
        elif arr.index(max_occurance) == 3:
            consensus += "T"
        else:
            print("Wrong index!")

    print(consensus)
    # print profile
    for arr in profile:
        for elem in arr:
            print(elem, end=" ")
        print()


file = "../resources/fasta3.txt"
make_profile(file)

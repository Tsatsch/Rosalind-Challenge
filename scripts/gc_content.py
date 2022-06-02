# Problem
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
# please see the note on absolute error below.

# alternative apporach
def gc_count(fastaname):
    # convert multiple line seq to one line
    seq_and_gc = {}  # {header : seq}
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
                    seq_and_gc[header.strip()] = seq
                    seq = ""
                    header = line[1:]
            else:
                seq += line.strip()

        seq_and_gc[header] = seq

        # count GC
        gc_content = {}  # {header : gc-percentage}
        for header, seq in seq_and_gc.items():
            count_c = seq.count("C")
            count_g = seq.count("G")
            perc = (count_c + count_g) / len(seq) * 100
            gc_content[header] = perc

        # print header and max gc
        for header, perc in gc_content.items():
            if perc == max(gc_content.values()):
                return header.strip(), gc_content[header]


fasta = "fasta4.txt"
header, gc = gc_count(fasta)
print(f"{header}\n{gc}")
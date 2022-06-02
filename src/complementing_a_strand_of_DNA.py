# Problem
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

def reverse_complement(dna):
    dna = dna.upper()
    reverse = ""

    for char in dna:
        if char == 'A':
            reverse += "T"
        elif char == 'C':
            reverse += "G"
        elif char == 'G':
            reverse += "C"
        elif char == 'T':
            reverse += "A"
        else:
            print("Worng nucelotide: " + char)
    return reverse[::-1]


print(reverse_complement("TAAGCCACGTGCCCCTACACAGTTCAGGGACACCGCATTATAGAGGCAGTAGACCGGTAGTCAACTAAAATTGCGGGCCGGTAGTTGAGAGGGTCCGTACTTAGCCCCGGCTCACGCGTAAATGTGCACAGGTTAAATAGTACTCAGATTGGCTTAGATTGCGCAGTGCATCTGCTGGTATATGACCAACCACGCAGAAGAGGCATGCCGAGCACCGTGGCCACTACTCCAAAAGCCCTTATGGGATATGTACATGTTACAGGCCAATTGTCGGCTATGGTCGTCATTGGGAATAGCTGGGGGGAGGGACTGGACATGTGCAAGCCCTAGCCGGACGGAACTACTTGGCACTGCTATCTGTAACAGCAGGGCTGGCACGGCAGTGGAGTTTCGATTAAGTAACCCGGACATAAAAAGTACCATTGATATGTAATACGTTTTTCGACCTAATCCAGAAGAAGAGTCTATTGTCCCTATGCCGAACCTCTATTCGTCACATAAACTACTCCGATGCATGATATGTCGGGGTTAATTGGCCATGTGTACCTTCGATTGTCTGTTCACGAACTTAAAATGTGTGTCCAACACTTTGGTCAACCGTAACTATGCTAATAGTTGCTAATACGCGATTGTACTAGGGACGCATTACGACTAACAGTCCTGAGGTTAACGGCTGCGCCGGCTGTCGCAGATGTCCCAAGCGCGATGGGCCCTTAGCTTCAAGAGGCGAGAAAGGTTGTCACTTACTTCTTATGAAGGGTAATACCTTCGGTCTGATACCTGCAAGTTTGTTTGCCGGTAAGAGGGATAAGCGTATGAAAGTGTGGCGATGCGCGTTATACGCCCACGCTTAGATCGCTTCGACTTCCCAAATATTCAGGTTAAAACCCCGGGTTCGTAAGGGGCGTCAACCAGGTTTGCGTCTCTCCGAAACGGGGCTCGCAGCTGCCCGGTGTGCACTATGCGGCTTGAGA"))

# Problem
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

def hamming_distance(s, t):
    d = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            d += 1
    return d


print(hamming_distance("ATGCCGACCGGCGATCAGAGTTATGGCATTGCACAGCCTAGCCCCTTCCTGTACTAACTCCAAGCTACTTCGAATAGACGCTAGGCAAGCCTCTTGCTTCTGCTGAACTGTCCAGACTATGCGCTGCGCTCAGCCTAACCGCGACGACCTGTGTTCGGAACCGTCGTTCTTAGGGTGGGCTATTTGGTCGCGTTCGTAGGAGTCAGCTGTCAAATGCAACACGGCGAACATAGGCTTAGCGCTAGTGTGGCGTCAAGCAAGACTAAGCCCAAATTTTTTAGAGGTCAGGCACTCCGATCTACACAGTTCTCGGGTCTCTTGAAATTCGTGGTCAGGCCACCAAGGACTGTGAAGGTCTGTTCTTGAAGGCCTCCTCCAAGGGCGTATGTCCAGTTGATGCGACGTTGACCATCCCTAAAGAAAACCCACGATCCATATTCGCACACATCTGAATCCACCGAAGGCTTACAGCAAGGCCAATCGATTTATTTATGCCATCCCCGCCACAACCGTTTTGTCAGATTTTTATGATCACCGCTACAGGCTTTGACTAGCTCTTCTTTTTTTAGAACTGACGCAAAGGATACCTGAGTTACTCCGGATTCTCCGAGAAGGAGTAGCAATCCGTAAGCGTTGTGCGATTGGGTGGGTATAACGCACGGGCCGGTTAGGGGCGTATCTGATGACTACGCGGTAAACTAAACGCTGTAAGAGCGTAGCCTGATCAAACACCTGGCAATTAGGCTGAGCTCCGGCCATAAAAACTCTGGGGCGTCCGCTAACTCAGAAACGTCCGCTAGATTACTTCCAGATTCCACGGTCGATCCCACCCCGAATCCTCTGTTACGGATGCCCGAAGGCATAAACAGCTCTGCCCCTATCCCGGAGGCGTCACAAACTTACGTGCCGCGTATATCCAGACTTCCCCCGGAGTAACAGCCCG",
                       "CTTATCTACGCGACTTGGCGTTTCGATCTAAATCTGACTCGCGGATTCCACTCCTAGCGCCTAGACTGCTGCAAACGAGCGACGACATGGCACAAGATATGGATCATTTTAGCAGTCTCTTAACCGCAATGCGGCTTTGCGGATCGTTCCGTTTTTCGAACCATAGTTCGAGAGCGGAATCCTTTCCTCCCATTCGAACGAATCCTGTAGCGGATTCAGTTTGGTGCGATCAGGCTTGGCCCAAATGTGGCGAAAGCCATGGCTTAGCATCATTTGACTGGTAAGCACCTTCTGGTGCCGAGACAGGCCGCGATTCTTTTAAAATTAGTGCGCAGGCCAAGTTAAAGAATGCAAGTCGATTTGTTCTAACCTCTTCCAATGTCTTTAGTTCTAACTATACCAATTACCGCACCGCTGAACAATAACCACCCTATACCTATCCAGGGCAGTGGACCAGCCCAACTTGCACGTCAATGCTAATCCCTACTTCCCTCCCAATTACACGCCGAACGTTGCGTGAGACAGTTAGCCCCCGAGCTCAAAACTATAACTGTAAGTTCCATTTTGTGACATGACACAAATGCTCCCTCACCTTCAACGTTTCAAGTGCGAACGTGTGCAAATACTCAAGCGTACACCTATCTGGTGGGCCTATCGAACGCACAGGTGATGTCCAAATATCATGGCATCCCTTGAACCTATAGAGTCAATATCCGTGGGTCGATCAACCCCCGGGGGACCTGACGGACATTCCGACTTAAATACTATCGTGTATCAGAAAACTCAGTAACCACCACTGGATTACTTGCGCACGCCAAAGTGGACCGGTCTAAGACATCCTTGTAAGGTTATACGTCCTGCAGTAACTGATCCGCCTTGAAGGCGAAGGGGCGTAATACGTCGTTGCAGCGTATGTCACTGCTACCCCCGTACAGACATATCG"))

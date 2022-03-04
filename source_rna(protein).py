def source_rna(protein):
    genetic_code_counts = {'F':2, 'L':6, 'I':3, 'M':1, 'V':4, 'S':6, 'P':4, 'T':4, 
                           'A':4, 'Y':2, 'H':2, 'Q':2, 'N':2, 'K':2, 'D':2, 'E':2, 
                           'C':2, 'W':1, 'R':6, 'G':4}
    combinations=1
    for letter in protein:
        combinations = combinations*genetic_code_counts[letter]
    combinations *= 3
    return combinations
        
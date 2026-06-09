
def reverse_complement(dna):
    comp={
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'     
        }
    result=""
    for ch in dna:
        result+=comp[ch]
    return result[::-1]
dna=input().strip()

print(reverse_complement(dna))

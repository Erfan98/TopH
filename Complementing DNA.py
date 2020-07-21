def reverse_complement(dna): 
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    return ''.join([complement[base] for base in dna[::-1]])


t=int(input())
for i in range(t):
    dna=input()
    print(reverse_complement(dna))
            
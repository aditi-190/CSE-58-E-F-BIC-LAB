
def most_kmers(text,k):
    freq = {}
    
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        freq[kmer]=freq.get(kmer, 0) +1
    max_count = max(freq.values())
    result=[]
    for kmer in freq:
            if freq[kmer] == max_count:
                result.append(kmer)            
    return result
text = input().strip()
k = int(input())

print(*most_kmers(text,k))

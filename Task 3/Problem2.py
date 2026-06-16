
def hamming(a,b):
    return sum(1 for i in range (len(a)) if a[i] != b[i])

def a_p_m(pattern, text, d):
    k=len(pattern)
    positions=[]
    
    for i in range(len(text)-k+1):
        window = text[i:i+k]
        if hamming(pattern,window) <= d:
            positions.append(i)
            
    return positions

pattern = input().strip()
text=input().strip()
d=int(input().strip())

result = a_p_m(pattern,text,d)
print(*result)

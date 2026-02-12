def first_unique_char(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c,0)+1
    
    for i, c in enumerate(s):
        if freq[c] ==1:
            return i
    return -1

print(first_unique_char("loveleetcode"))
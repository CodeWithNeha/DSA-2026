from collections import deque
def firstNonRe(stream):
    result = []
    freq = {}
    
    for ch in stream:
        freq[ch] = freq.get(ch,0)+1
        q = deque()

        q.append(ch)
        while q and freq[q[0]]>1:
            q.popleft()
        result.append(q[0] if q else -1)
    return result

print(firstNonRe("aabc"))
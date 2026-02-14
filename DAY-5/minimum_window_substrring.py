from collections import Counter

def minWindow(s, t):
    if not t:
        return ""

    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0

    left = 0
    res = [-1, -1]
    res_len = float("inf")

    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1

        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < res_len:
                res = [left, right]
                res_len = right - left + 1

            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1

            left += 1

    l, r = res
    return "" if res_len == float("inf") else s[l:r+1]

s = "ADOBECODEBANC" 
t = "ABC"
print(minWindow(s,t))

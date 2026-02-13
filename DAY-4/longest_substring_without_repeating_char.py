def longest_substring(str):
    seen = set()
    l = 0
    ans = 0
    for r in range(len(str)):
        while str[r] in seen:
            seen.remove(str[l])
            l+=1
        seen.add(str[r])
        print(seen)
        ans = max(ans, r-l+1)
    return ans

print(longest_substring("abcabcbb"))
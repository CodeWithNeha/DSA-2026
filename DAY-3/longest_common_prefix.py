def longest_common_prefix(s):
    if not s:
        return ""
    
    for i in range(len(s[0])):
        char = s[0][i]
        for word in s[1:]:
            if i == len(word) or char!=word[i]:
                return s[0][:i]
    return s[0]

# print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","car","racecar"]))